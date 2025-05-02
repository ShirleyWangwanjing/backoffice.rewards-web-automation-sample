import os
import shutil
import tempfile
import uuid

import yaml
from allure import attach
from allure import attachment_type
from behave import fixture
from behave.textutil import text
from page_model.logout import Logout
from page_model.okta_page import OktaPage
from utils.yml_data import YMLData
from utils import logger
import time
from utils.get_console_log import GetConsoleLog
from utils.date_utils import DateUtils
from utils.file_utils import FileUtils
import base64
import json

STORE_LOCATION = os.path.join(
    tempfile.gettempdir(),
    '.store.force'
)


class BehavePatcher(object):
    def __init__(self):
        pass

    def __init__(self, context, step):
        self.context, self.step = context, step

    def insert_png_to_allure_report(self, name='Screenshot'):
        name = 'Screenshot'
        if not hasattr(self.context, 'browser'):
            return
        if self.context.browser:
            try:
                attach(
                    name=name,
                    body=self.context.browser.get_screen_shot_as_png(),
                    attachment_type=attachment_type.PNG
                )
            except Exception as e:
                raise RuntimeError(
                    'Failed to insert screenshot to allure report, due to: '+e
                )

    def insert_log_to_allure_report(self, name, log_list):
        attachment_body = ''
        for log in log_list:
            attachment_body = attachment_body + yaml.dump(log)
        try:
            attach(
                name=name,
                body=attachment_body,
                attachment_type=attachment_type.YAML
            )
        except Exception as e:
            raise RuntimeError(
                'Failed to insert log to allure report, due to: ' + e
            )

    def insert_dict_log_to_allure_report(self, name, log_dict):
        attachment_body = json.dumps(log_dict)
        try:
            attach(
                name=name,
                body=attachment_body,
                attachment_type=attachment_type.YAML
            )
        except Exception as e:
            raise RuntimeError(
                'Failed to insert log to allure report, due to: ' + e
            )

    def insert_har_allure_report(self, name, har_json_text):
        # attachment_body = json.dumps(har_file)
        logger.info("start insert har")
        try:
            attach(
                name=name,
                body=har_json_text,
                attachment_type=attachment_type.TEXT
            )
        except Exception as e:
            raise RuntimeError(
                'Failed to insert har to allure report, due to: ' + e
            )
        logger.info("finished insert har")


def setup_all(context):
    context.data, context.loaded_yml_files = load_context_data()

    if 'features' not in vars(context.data):
        context.data = YMLData(
            **dict(features=[])
        )

    if not os.path.exists(STORE_LOCATION):
        os.makedirs(STORE_LOCATION)

    return context.data


# def teardown_all(context):
#     clean_up_test_data(context.data)
#     save_context_data(context.data)
#     remove_obsolete_files(
#         context.loaded_yml_files
#     )


def setup_feature(context, feature):
    names = [
        _feature.name
        for _feature in context.data.features
    ]

    if feature.name not in names:
        context.data.features += [
            dict(
                name=feature.name,
                scenarios=[]
            )
        ]
    else:
        if feature.name != names[-1]:
            _feature = context.data.features.pop(
                names.index(feature.name)
            )
            context.data.features.append(_feature)

    return context.data.features[-1]


def teardown_feature(context, feature):
    context.data.features[-1].status = feature.status.name
    stop_chrome_proxy_server(context,feature)


def setup_scenario(context, scenario):
    feature = context.data.features[-1]

    names = [
        _scenario.name
        for _scenario in feature.scenarios
    ]

    if scenario.name not in names:
        feature.scenarios += [
            dict(name=scenario.name)
        ]
    else:
        if scenario.name != names[-1]:
            _scenario = feature.scenarios.pop(
                names.index(scenario.name)
            )

            feature.scenarios.append(_scenario)

    return context.data.features[-1].scenarios[-1]


# def log_out_from_ui(context, scenario):
#     if not hasattr(context, "browser"):
#         return
#     try:
#         home_page = Logout(context)
#         home_page.logout(scenario.name)
#         time.sleep(1)
#     except Exception as e:
#         logger.info(scenario.name+" logout fail, exception:"+str(e))

def login_from_ui(context, feature):
    if not hasattr(context, "browser"):
        return
    try:
        home_page = OktaPage(context)
        home_page.okta_ui_login(feature.name)
        time.sleep(1)
    except Exception as e:
        logger.info(feature.name+" login fail, exception:"+str(e))


def log_out_from_ui(context, feature):
    if not hasattr(context, "browser"):
        return
    try:
        home_page = Logout(context)
        home_page.logout(feature.name)
        time.sleep(1)
    except Exception as e:
        logger.info(feature.name+" logout fail, exception:"+str(e))

def back_to_campaign(context, feature):
    if not hasattr(context, "browser"):
        return
    try:
        home_page = OktaPage(context)
        home_page.back_to_campaign_tab(feature.name)
    except Exception as e:
        logger.info(feature.name+" back to campaign tab, exception:"+str(e))


def save_failure_test_cases(context, scenario):
    if scenario.status != "passed":
        with open ("failing_case_list.txt","a") as f:
            f.write(scenario.name + "\n")

def take_snapshot_for_ui(context, scenario):
    if not hasattr(context, "browser"):
        return
    scenario_data = context.data.features[-1].scenarios[-1]
    if scenario.status.name != 'passed':
        BehavePatcher(context, scenario).insert_png_to_allure_report("Fail Step Screenshot")


def attach_ui_console_log(context, scenario):
    console_log = GetConsoleLog(context).get_console_log()
    if len(console_log) == 0:
        return
    # if scenario.status.name != 'passed':
    BehavePatcher(context, scenario).insert_log_to_allure_report("brower_console_log", console_log)


def get_har(context, scenario):
    if hasattr(context, "browser") and ('withproxy' in context.browser_type.lower()):
        har = context.browser.chrome_proxy.har
        har_json = json.dumps(har, indent=2)
        BehavePatcher(context, scenario).insert_har_allure_report(scenario.name+' har_file', har_json)
        context.browser.chrome_proxy.har.clear()

# def store_har_file(title, result):
#     """store result"""
#     har_file = open(title+'.har', 'w', encoding='utf-8')
#     har_file.write(str(result))
#     har_file.close()


def stop_chrome_proxy_server(context, feature):
    if hasattr(context, "browser") and ('withproxy' in context.browser_type.lower()):
        context.browser.chrome_proxy_server.stop()


def teardown_scenario(context, scenario):
    scenario_data = context.data.features[-1].scenarios[-1]
    if scenario_data:
        scenario_data.status = scenario.status.name
        # attach(
        #     name=text(scenario_data.name),
        #     body=yaml.dump(scenario_data),
        #     attachment_type=attachment_type.YAML,
        #     extension='yml'
        # )


@fixture
def fixture_all(context):
    setup_all(context)

    yield

    # teardown_all(context)


@fixture
def fixture_feature(context, feature):
    context.logger.info(
        'RUNNING - Feature: {}'.format(feature.name)
    )
    setup_feature(context, feature)
    yield
    teardown_feature(context, feature)


@fixture
def fixture_scenario(context, scenario):
    context.logger.info(
        'RUNNING - Scenario: {}'.format(scenario.name)
    )
    setup_scenario(context, scenario)
    yield
    take_snapshot_for_ui(context, scenario)
    attach_ui_console_log(context, scenario)
    get_har(context, scenario)
    # back_to_campaign(context, scenario)
    #log_out_from_ui(context, scenario)
    # clean_up_scenario_data(context, scenario)
    save_failure_test_cases(context, scenario)
    teardown_scenario(context, scenario)
    context.logger.info(
        '{} - Scenario: {}'.format(
            scenario.status.name.upper(),
            scenario.name
        )
    )
    time.sleep(0.5)


def remove_obsolete_files(files):
    for fp in files:
        try:
            if os.path.exists(fp):
                os.remove(fp)
        except IOError as ioe:
            logger.warning(ioe)
        except Exception as ex:
            logger.error(ex)


def remove_empty_directory(
        location=STORE_LOCATION
):
    try:
        if not os.listdir(location):
            shutil.rmtree(
                location,
                ignore_errors=True
            )
    except FileNotFoundError:
        logger.debug(
            'YML file directory ({}) was not found'.format(
                location
            )
        )


def save_context_data(data):
    remove_empty_directory()

    if not data:
        return

    if not isinstance(data, YMLData):
        raise TypeError(
            'Invalid context data'
        )

    try:
        if not os.path.exists(STORE_LOCATION):
            os.makedirs(STORE_LOCATION)

        dump_file = os.path.join(
            STORE_LOCATION,
            '{}.yml'.format(uuid.uuid4())
        )

        data.dump(dump_file)
    except:
        raise

    return dump_file


def load_context_data(
        file_location=STORE_LOCATION
):
    context_data = YMLData()
    loaded_files = []

    try:
        if file_location and os.path.exists(file_location):
            for root, _, files in os.walk(file_location):
                for file in files:
                    yml_file = os.path.join(root, file)

                    context_data += context_data.load(
                        yml_file
                    )

                    loaded_files.append(yml_file)
    except:
        pass

    return context_data, loaded_files

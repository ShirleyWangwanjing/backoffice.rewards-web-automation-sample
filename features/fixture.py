import os
import sys
import urllib3

from behave import fixture

from configs.mobile import ConfigMobile
from configs.zalenium import ConfigZalenium
from page_model.okta_page import OktaPage
from ui.browser import BrowserType, Browser
from ui.browser_manager import BrowserManager
from utils.config_manager import ConfigManager
from utils.session_manager import BaseSession
from utils.sql_database_manager import SqlDatabaseManager
from utils import logger


@fixture
def fixture_browser(context, tag, *args, **kwargs):
    user_browser_tag = ""
    if hasattr(context, "user_browser_tag"):
        user_browser_tag = context.user_browser_tag

    project_tag = tag[tag.rindex('.') + 1:]
    context.ui_config = context.test_config['ui'][project_tag]

    try:
        context.browserManager = BrowserManager()
        if user_browser_tag == 'appium':
            browser_type = BrowserType.APPIUM
            context.browserManager.add_browser_queue(
                Browser(
                    base_url=context.ui_config['base_url'],
                    browser_type=browser_type,
                    command_executor=ConfigMobile.appium_command_Executor,
                    desired_capabilities=ConfigMobile.android_desired_capabilities
                )
            )
        else:
            # if True:
            if os.environ.get('AUTOMATION_DOCKER_ENV') is not None:
                logger.info(" set AUTOMATION_DOCKER_ENV")
                browser_type = BrowserType.HEADLESS_CHROME
                # browser_type = BrowserType.HEADLESS_CHROME_WITH_PROXY
                logger.info("browser_type=" + browser_type)
            elif os.environ.get('DOCKER_ENV_ZALENIUM') is not None:
                logger.info(" set DOCKER_ENV_ZALENIUM")
                browser_type = 'zalenium'
                logger.info("browser_type=" + browser_type)
            else:
                browser_type = context.ui_config['browser']
                logger.info("browser_type=" + browser_type)

            if sys.platform.startswith('Linux'):
                exec_path = '/usr/bin/google-chrome'
                os.environ['webdriver.chrome.driver'] = \
                    exec_path
                context.executable_path = exec_path

                context.browserManager.add_browser_queue(
                    Browser(
                        base_url=context.ui_config['base_url'],
                        browser_type=browser_type,
                        executable_path=exec_path
                    )
                )
            if browser_type == 'zalenium':
                logger.info("@_@ zelenium desktop")
                urllib3.disable_warnings()
                browser = context.config.userdata.get('browser', 'chrome')
                caps = ConfigZalenium.availableCaps.get(browser)
                if caps is None:
                    raise Exception('unsupported browser' + browser)
                caps["sauce:options"]["name"] = context.data.features[-1].name + ' - ' + caps["browserName"]
                context.browserManager.add_browser_queue(
                    Browser(
                        base_url=context.ui_config['base_url'],
                        browser_type=browser_type,
                        command_executor=ConfigZalenium.zalenium_command_executor,
                        desired_capabilities=caps
                    )
                )
            else:
                context.browserManager.add_browser_queue(
                    Browser(base_url=context.ui_config['base_url'], browser_type=browser_type)
                )

            context.browser_type = browser_type
            context.browser = context.browserManager.get_browser()
            context.browser.maximize_window()
            login_page = OktaPage(context)
            attempts = 3
            while attempts > 0:
                try:
                    login_page.load()
                    login_page.okta_ui_login()
                    break
                except Exception as e:
                    logger.error("Error is{}".format(e))
                    attempts -= 1
                    continue
        yield context.browser
    finally:
        if context.browser:
            context.browser.quit()

        if context.browserManager:
            context.browserManager.clear_browsers()


@fixture
def fixture_sql_database(context, tag, *args, **kwargs):
    sql_db_config_dict = context.test_config['sql_database']
    host = sql_db_config_dict['server']
    user = sql_db_config_dict['user']
    pwd = sql_db_config_dict['password']
    database_promo = sql_db_config_dict['database_promos']
    database_rewards = sql_db_config_dict['database_rewards']
    try:
        promo_database = SqlDatabaseManager(host, user, pwd, database_promo)
        rewards_database = SqlDatabaseManager(host, user, pwd, database_rewards)
        promo_database.connect_database()
        rewards_database.connect_database()
        context._root['promo_database'] = promo_database
        context._root['rewards_database'] = rewards_database
    finally:
        pass


@fixture
def fixture_api_session(context, tag, *args, **kwargs):
    tag = tag[tag.rindex('.') + 1:]
    api_config_dict = context.test_config['api'][tag]

    base_url = api_config_dict['base_url']
    # username = api_config_dict['username']
    # password = api_config_dict['password']

    api_session = BaseSession(base_url)
    # if username and password:
    #     api_session.set_auth()
    context.api_session = api_session


@fixture
def fixture_test_configuration(context):
    ConfigManager().add_config_context(context)

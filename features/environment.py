# -*- coding: utf-8 -*-
import os

from behave.fixture import fixture_call_params
from behave.fixture import use_composite_fixture_with
from behave.fixture import use_fixture

from features.fixture import fixture_browser
from features.fixture import fixture_sql_database
from features.fixture import fixture_api_session
from features.fixture import fixture_test_configuration

from features.fixture_context import fixture_all
from features.fixture_context import fixture_feature
from features.fixture_context import fixture_scenario
from page_model.clear_campaign import ClearCampaign

from utils import logger

from fnmatch import fnmatchcase


class FixtureInitiator(object):
    def __init__(self, context, feature):
        self.context, self.feature = context, feature

    def init_fixture(self):
        tags = self.feature.tags
        for tag in tags:
            if fnmatchcase(tag, '*.sql_database.*'):
                use_composite_fixture_with(
                    self.context, (
                        fixture_call_params(fixture_sql_database, tag),
                    )
                )
            if fnmatchcase(tag, '*.api.*'):
                use_composite_fixture_with(
                    self.context, (
                        fixture_call_params(fixture_api_session, tag),
                    )
                )
            if fnmatchcase(tag, '*.browser.*'):
                use_composite_fixture_with(
                    self.context, (
                        fixture_call_params(fixture_browser, tag),
                    )
                )


def before_step(context, step):
    pass


def before_scenario(context, scenario):
    use_composite_fixture_with(
        context, (
            fixture_call_params(
                fixture_scenario,
                scenario
            ),
        )
    )


def before_feature(context, feature):
    use_composite_fixture_with(
        context, (
            fixture_call_params(
                fixture_feature,
                feature
            ),
        )
    )
    fixture_initiator = FixtureInitiator(context, feature)
    fixture_initiator.init_fixture()


def before_all(context):
    os.environ["HTTPS_PROXY"]="http://127.0.0.1:8086"
    context.logger = logger
    context.logger.setLevel(
        context.config.logging_level
    )

    use_fixture(
        fixture_all, context
    )

    use_fixture(
        fixture_test_configuration, context
    )


def after_all(context):
    if hasattr(context, 'promo_database') and hasattr(context, 'rewards_database'):
        clear_campaign = ClearCampaign()
        clear_campaign.clear_data_via_sql_file(os.path.join(os.getcwd(), 'configs', 'clearpromoData.sql'),
                                               context.promo_database)
        clear_campaign.clear_data_via_sql_file(os.path.join(os.getcwd(), 'configs', 'clearRewardCampaignData.sql'),
                                               context.rewards_database)
        # clear_campaign.clear_Refresh_redis_cache()
        context.promo_database.close_database()
        context.rewards_database.close_database()


# if __name__ == '__main__':
#     clear_campaign = ClearCampaign()
#     clear_campaign.clear_data_via_sql_file('/Users/junying.li/backoffice.rewards-web-automation/configs/clearpromoData.sql', self.context.promo_database)
#     clear_campaign.clear_data_via_sql_file('/Users/junying.li/backoffice.rewards-web-automation/configs/clearRewardCampaignData.sql', context.promo_database)
#     # clear_campaign.clear_Refresh_redis_cache()

# -*- coding: utf-8 -*-

from page_model.home import TabBar

from page_model.login import Login
from page_model.okta_page import OktaPage
from behave import then, given

from page_model.logout import Logout
from utils.yml_data import YMLData
from utils import logger
import time


def _load_cookies(browser, filename):
    for cookie in getattr(
            YMLData.load(filename),
            'cookies', []
    ):
        try:
            browser.add_cookie(vars(cookie))
        except Exception as ex:
            logger.error(ex)


@given('{login_user} can enter the username and password')
def step_impl(context, login_user):
    # context.login_user = login_user
    # login_page = Login(context)
    # login_page.load().ui_login()

    context.login_user = login_user
    okta_login_page = OktaPage(context)
    okta_login_page.load().okta_ui_login()


@then('I can see the rewards campaigns page')
def step_impl(context):
    context.tabs_page = TabBar(context)
    context.tabs_page.check_rewards_campaigns_tab()


@given('Logout the current user')
def step_logout(context):
    Logout(
        context.browser
    ).logout()


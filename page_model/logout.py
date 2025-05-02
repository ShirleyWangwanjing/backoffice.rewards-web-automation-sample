# -*- coding: utf-8 -*-
from selenium.webdriver.common.by import By
from ui.base import Base
from utils import logger


class Logout(Base):
    logout_button_by = (By.XPATH, '//a[@data-qa-element="bui-header-logout-button"]')
    logout_text_by = (By.XPATH,'//*[contains(text(), "now logged out")]')

    def logout(self, scenario_name):
        logout_successfully = False

        retry = 5
        self.context.browser.get_webdriver().maximize_window()
        while (logout_successfully is False) and (retry > 0):
            self.page_operation.click_element(self.logout_button_by)
            logout_successfully = self.page_operation.element_visible(self.logout_text_by, 30)
            retry = retry - 1
        if logout_successfully is False:
            logger.info("..................."+scenario_name+": log out fail")

    @property
    def is_logged_in(self):
        return self.page_operation.element_exists(
            self.Locators.mnu_user_panel
        )

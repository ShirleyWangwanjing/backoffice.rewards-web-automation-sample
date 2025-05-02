from selenium.webdriver.common.by import By
import time
from features.fixture_context import BehavePatcher


class FormOperation(object):
    def __init__(self, context, page_operation):
        self.context = context
        self.page_operation = page_operation

    def click_drop_down_menu(self, dropdown_by, option_by, interval=2):
        self.page_operation.element_visible(dropdown_by)

        def until_dropdown_condition():
            return self.page_operation.element_visible(option_by, interval)
        self.page_operation.click_element(dropdown_by, until_dropdown_condition, interval=interval)

        def until_option_condition():
            return self.page_operation.element_visible(option_by, interval) is False
        self.page_operation.click_element(option_by, until_option_condition, interval=interval)

    def button_is_clickable(self, button_by):
        pass

    def button_is_disable(self, button_by):
        pass

    def click_button(self, button_by, until_condition):
        self.page_operation.click_element(
            (By.XPATH, button_by,),
            until_condition
        )

    def set_checkbox_true(self, checkbox_by, until_condition=None):
        self.click_checkbox(checkbox_by, until_condition)

    def set_checkbox_false(self,checkbox_by, until_condition=None):
        self.click_checkbox(checkbox_by, until_condition)

    def click_checkbox(self, checkbox_by, until_condition=None):
        self.page_operation.click_element(
            (By.XPATH, checkbox_by,),
            until_condition
        )

    def set_radio_button_true(self, radio_button_by, until_condition=None):
        self.click_checkbox(radio_button_by, until_condition)

    def set_radio_button_false(self, radio_button_by, until_condition=None):
        self.click_checkbox(radio_button_by, until_condition)

    def click_radio_button(self, radio_button_by, until_condition=None):
        self.page_operation.click_element(
            (By.XPATH, radio_button_by,),
            until_condition
        )
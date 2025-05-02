# -*- coding: utf-8 -*-
import time
from ui.page_operation import PageOperation
from selenium.webdriver.common.by import By


class Base(object):
    products_text_exist = (By.XPATH, '//div[text()="Product(s)"]')
    cart_icon = (By.CLASS_NAME, 'cart-qty')
    default_check_element_exist_time_out = 10
    apply_code_text_exist = (By.ID, 'applyPromoCode')
    icon_sadness = (By.CLASS_NAME, 'icon-sadness')

    def __init__(self, context):
        self.context = context
        self.page_operation = PageOperation(context)

    def load(self):
        """
        To load the page
        """
        pass

    def open_url(self):
        """
        To open the url
        """
        self.page_operation.go_to_url()

    def get_driver(self):
        """
        to get the driver
        :return: browser
        """
        return self.context.browser

    @staticmethod
    def hard_sleep(seconds):
        """
        Do the smart wait for a particular seconds
        :param seconds: Seconds to wait
        """
        time.sleep(seconds)

    def refresh_cart_until_not_crash(self):
        def condition1():
            return not self.page_operation.element_visible(
                self.icon_sadness,
                self.default_check_element_exist_time_out
            )

        self.page_operation.click_element(self.cart_icon, until_condition=condition1)


# -*- coding: utf-8 -*-
__author__ = 'Ragu.Sekaran'

from selenium.common.exceptions import TimeoutException
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.ie.webdriver import DEFAULT_TIMEOUT


class WaitUtils(object):
    interval = 0.5
    timeout = 30.0

    @staticmethod
    def wait_for_elements_present(
            driver, locator,
            interval=interval, timeout=timeout
    ):
        return WebDriverWait(
            driver, timeout, interval
        ).until(
            EC.presence_of_all_elements_located(locator)
        )

    @staticmethod
    def wait_for_elements_visible(
            driver, locator,
            interval=interval, timeout=timeout
    ):
        return WebDriverWait(
            driver, timeout, interval
        ).until(
            EC.visibility_of_all_elements_located(locator)
        )

    # @staticmethod
    # def wait_for_elements_visible(
    #         driver, locator,
    #         interval=interval, timeout=timeout
    # ):
    #     return WebDriverWait(
    #         driver, timeout, interval
    #     ).until(
    #         EC.visibility_of_all_elements_located(locator)
    #     )

    @staticmethod
    def wait_for_element_invisible(
            driver,
            locator,
            interval=interval, timeout=timeout
    ):
        return WebDriverWait(
            driver, timeout, interval
        ).until(
            EC.invisibility_of_element_located(locator)
        )

    @staticmethod
    def wait_for_element_clickable(
            driver, locator,
            interval=interval, timeout=timeout
    ):
        return WebDriverWait(
            driver, timeout, interval
        ).until(
            EC.element_to_be_clickable(locator)
        )

    @staticmethod
    def wait_for_frame_available(
            driver, locator,
            interval=interval, timeout=timeout
    ):
        return WebDriverWait(
            driver, timeout, interval
        ).until(
            EC.frame_to_be_available_and_switch_to_it(
                locator
            )
        )

    @staticmethod
    def wait_for_alert_presents(
            driver, interval=interval, timeout=timeout
    ):
        return WebDriverWait(
            driver, timeout, interval
        ).until(
            EC.alert_is_present()
        )

    @staticmethod
    def wait_for_element_presents(
            driver, element,
            interval=interval, timeout=timeout
    ):
        return WebDriverWait(
            driver, timeout, interval
        ).until(
            EC.visibility_of(element)
        )

    # @staticmethod
    # def wait_for_element_unpresent(
    #         driver, locator,
    #         interval=interval, timeout=timeout
    # ):
    #     return WebDriverWait(
    #         driver, timeout, interval
    #     ).until_not(
    #         EC.presence_of_all_elements_located(locator)
    #     )

    @staticmethod
    def wait_element_to_be_visible(driver, locator, timeout=DEFAULT_TIMEOUT):
        try:
            WebDriverWait(driver, timeout).until(EC.visibility_of_element_located(locator))
            return True
        except TimeoutException:
            return False
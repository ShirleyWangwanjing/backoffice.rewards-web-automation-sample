__author__ = 'Ragu.Sekaran'

from selenium.webdriver.common.by import By
from ui.base import Base
import allure


class TabBar(Base):
    rewards_campaigns_tab = (By.CSS_SELECTOR, 'a[data-qa-element="brm-campaigns-top-nav-nav-link-rewards-campaigns"]')

    # Check rewards campaigns tab
    @allure.step
    def check_rewards_campaigns_tab(self):
        self.hard_sleep(7)
        assert self.page_operation.element_exists(TabBar.rewards_campaigns_tab)

    # Click rewards campaigns tab
    @allure.step
    def click_rewards_campaigns_tab(self):
        self.hard_sleep(15)
        self.page_operation.click_element(TabBar.rewards_campaigns_tab)

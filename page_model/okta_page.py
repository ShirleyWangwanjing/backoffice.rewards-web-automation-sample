import allure
from ui.base import Base
from configs.password import environment_password
from selenium.webdriver.common.by import By


class OktaPage(Base):
    # PageObject definition
    input_username = (By.CSS_SELECTOR, 'input[id="okta-signin-username"]')
    input_password = (By.CSS_SELECTOR, 'input[id="okta-signin-password"]')
    button_signin = (By.CSS_SELECTOR, '#okta-signin-submit')
    button_campaign = (By.CSS_SELECTOR, 'div[data-qa-element="brm-campaigns-list-tabs"] div[data-qa-element="bui-label-item-0"]')

    def load(self):
        self.page_operation.go_to_url()
        return self

    @allure.step
    def username(self, value):
        self.page_operation.input_element(self.input_username, value)

    @allure.step
    def password(self, value):
        self.page_operation.input_element(self.input_password, value)

    @allure.step
    def sign_in(self):
        self.page_operation.click_element(self.button_signin)

    @allure.step
    def okta_ui_login(self):
        username = self.context.ui_config['test_user']["test_user_editor"]['Username']
        password = self.context.ui_config['test_user']["test_user_editor"]['Password']
        self.username(username)
        self.password(password)
        self.sign_in()
        self.hard_sleep(15)

    @allure.step
    def okta_ui_logout(self):
        username = self.context.ui_config['test_user']["test_user_editor"]['Username']
        password = self.context.ui_config['test_user']["test_user_editor"]['Password']
        self.username(username)
        self.password(password)
        self.sign_in()

    @allure.step
    def back_to_campaign_tab(self):
        self.page_operation.click_element(self.button_campaign)
        self.hard_sleep(2)


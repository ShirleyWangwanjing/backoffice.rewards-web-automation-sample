__author__ = 'Ragu.Sekaran'

import allure

from ui.base import Base
from configs.password import environment_password
from selenium.webdriver.common.by import By


class Login(Base):
    # PageObject definition
    input_username = (By.ID, 'username')
    input_password = (By.ID, 'password')
    button_signin = (By.CSS_SELECTOR, 'div> button[class="btn btn-primary w100P"]')

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
    def ui_login(self):
        login_user = self.context.login_user
        username = self.context.ui_config['test_user'][login_user]['Username']
        password = environment_password()

        self.username(username)
        self.password(password)
        self.sign_in()


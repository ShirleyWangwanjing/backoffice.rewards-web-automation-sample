from telnetlib import EC
from selenium.common.exceptions import TimeoutException
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from page_model.campaigns.form import Form
from selenium.webdriver.common.by import By
from ui.base import Base
import allure
import time


class List(Base):
    # tabs
    campaigns_tab = (By.CSS_SELECTOR, 'div[data-qa-element="brm-campaigns-list-tabs"] div[data-qa-element="bui-label-item-0"]')
    r_code_tab = (By.CSS_SELECTOR, 'div[data-qa-element="brm-campaigns-list-tabs"] div[data-qa-element="bui-label-item-1"]')
    r_code_tab_flag = (By.XPATH, '//div[text()="Rcode"]')
    shipping_credit_tab = (By.CSS_SELECTOR, 'div[data-qa-element="brm-campaigns-list-tabs"] div[data-qa-element="bui-label-item-2"]')
    shipping_credit_tab_flag = (By.XPATH, "//div[@data-qa-element='brm-campaigns-search-criteria-auto-suggestion-r-code']")
    archived_tab = (By.XPATH, '//div[text()="ARCHIVED"]')
    # search countries and names
    search_countries_and_names_input = (By.CSS_SELECTOR, 'div[data-qa-element="brm-campaigns-search-criteria-auto-suggestion-search"] input')
    search_countries_and_names_option = (By.CSS_SELECTOR, 'div[data-qa-element="brm-campaigns-search-criteria-auto-suggestion-search"] div[data-qa-element="bui-result-list"] div[data-qa-element="bui-result-item-0"]')
    # search referral code
    search_r_code_input = (By.CSS_SELECTOR, 'div[data-qa-element="brm-campaigns-search-criteria-auto-suggestion-r-code"] input')
    search_r_code_option = (By.CSS_SELECTOR, 'div[data-qa-element="brm-campaigns-search-criteria-auto-suggestion-r-code"] div[data-qa-element="bui-result-list"] div[data-qa-element="bui-result-item-0"]')
    # status
    status_drop_down = (By.CSS_SELECTOR, 'div[data-qa-element="brm-campaigns-search-criteria-drop-down-list-status"] div[data-qa-element="bui-value-wrapper"] > div')
    pending_approval_drop_down_option = (By.CSS_SELECTOR, 'div[data-qa-element="brm-campaigns-search-criteria-drop-down-list-status"] div[data-qa-element="bui-option-list"] div[data-qa-element="bui-option-item-1"]')
    deactivated_drop_down_option = (By.CSS_SELECTOR, 'div[data-qa-element="brm-campaigns-search-criteria-drop-down-list-status"] div[data-qa-element="bui-option-list"] div[data-qa-element="bui-option-item-2"]')
    # date range
    txt_start_date = (By.CSS_SELECTOR, 'div[data-qa-element="brm-campaigns-search-criteria-range-date-picker-date-range"] div[data-qa-element="bui-startdate"] div[data-qa-element="bui-textbox"]')
    txt_end_date = (By.CSS_SELECTOR, 'div[data-qa-element="brm-campaigns-search-criteria-range-date-picker-date-range"] div[data-qa-element="bui-enddate"] div[data-qa-element="bui-textbox"]')
    btn_search = (By.CSS_SELECTOR, 'button[data-qa-element="brm-campaigns-search-criteria-button-search"]')
    btn_clear = (By.CSS_SELECTOR, 'button[data-qa-element="brm-campaigns-search-criteria-button-clear"]')
    start_date_calendar = (By.CSS_SELECTOR, 'div[data-qa-element="brm-campaigns-search-criteria-range-date-picker-date-range"] div[data-qa-element="bui-startdate"] svg')
    end_date_calendar = (By.CSS_SELECTOR, 'div[data-qa-element="brm-campaigns-search-criteria-range-date-picker-date-range"] div[data-qa-element="bui-enddate"] svg')
    # buttons
    btn_create_new_btn = (By.CSS_SELECTOR, 'button[data-qa-element="brm-campaigns-search-criteria-button-create-new"]')
    # list
    list_container = (By.CSS_SELECTOR, 'div[data-qa-element="brm-campaigns-list-container"]')
    campaign_name_in_list_xpath = "//div[@data-qa-element='brm-campaigns-list-container']//div[text()='{}']"
    first_campaign = (By.CSS_SELECTOR, 'div[data-qa-element="brm-campaigns-list-card-0"]')
    year_calendar_drop_down = (By.XPATH, '//div[@data-qa-element="bui-month-dropdown"]')
    tag_name = (By.TAG_NAME, 'body')
    campaign_name_link_xpath = "//div[@data-qa-element='brm-campaigns-list-container']//div[contains(text(),'{}')]"
    save_btn = (By.CSS_SELECTOR, 'button[data-qa-element="brm-campaigns-form-header-button-save"]')
    reward_type = (By.XPATH, '//div[@data-qa-element="brm-campaigns-list-card-data-row-0"]/div[2]')
    status_first_created = (By.XPATH, '//div[@data-qa-element="brm-campaigns-list-card-data-row-0"]/div[4]')
    of_countries = (By.XPATH, '//div[@data-qa-element="brm-campaigns-list-card-data-row-0"]/div[6]')
    N1 = (By.XPATH, '//div[@data-qa-element="brm-campaigns-list-data-column-tag-n-1"]')
    E1 =(By.XPATH, '//div[@data-qa-element="brm-campaigns-list-data-column-tag-e-1"]')
    first_campaign_row = (By.XPATH, '//div[@data-qa-element="brm-campaigns-list-card-data-row-0"]')


    @allure.step
    def click_list_view_campaigns_tab(self):
        self.page_operation.click_element(self.campaigns_tab)
        self.hard_sleep(8)

    @allure.step
    def click_list_view_r_code_tab(self):
        self.hard_sleep(20)
        self.page_operation.click_element(self.r_code_tab)
        self.hard_sleep(10)
        # rcode_page_show = self.page_operation.element_visible(self.r_code_tab_flag, 2)
        # assert rcode_page_show is True, "Go to rcode tab fail"

    @allure.step
    def click_list_view_shipping_credit_tab(self):
        retry = 5
        load_successfully = False
        while (retry >= 0) and (load_successfully is False):
            load_successfully = self.page_operation.element_visible(self.shipping_credit_tab, 30)
            self.context.browser.get_webdriver().refresh()
            self.hard_sleep(5)
            retry = retry - 1

        def until_condition():
            return self.page_operation.element_visible(self.shipping_credit_tab_flag, 10)
        self.page_operation.click_element(self.shipping_credit_tab, until_condition)
        self.hard_sleep(5)

        self.page_operation.element_visible(self.shipping_credit_tab_flag)

    @allure.step
    def click_list_view_archived_tab(self):
        self.page_operation.click_element(self.archived_tab)
        try:
            WebDriverWait(self.page_operation.driver, 60).until(EC.visibility_of_element_located(self.first_campaign_row))
        except TimeoutException:
            raise TimeoutException('after clicking archived button 60s, campaign list page not loaded well so Element is not clickable')

    @allure.step
    def search_country_or_campaign_name_or_rcode(self):
        if self.page_operation.element_exists(self.search_countries_and_names_input, 5):
            generated_campaign_name = Form.generatedCampaignName[-1]
            self.page_operation.input_element(self.search_countries_and_names_input, generated_campaign_name)
        if self.page_operation.element_exists(self.search_r_code_input, 5):
            generated_rcode = Form.generatedRcode[-1]
            self.page_operation.input_element(self.search_r_code_input, generated_rcode)
        self.hard_sleep(3)


    @allure.step
    def select_search_country_or_campaign_name_option(self):
        self.page_operation.click_element(self.search_countries_and_names_option)
        self.hard_sleep(15)

    @allure.step
    def click_status_drop_down(self):
        self.page_operation.click_element(self.status_drop_down)

    @allure.step
    def click_pending_approval_drop_down_option(self):
        self.page_operation.click_element(self.pending_approval_drop_down_option)

    @allure.step
    def click_deactivated_drop_down_option(self):
        self.page_operation.click_element(self.deactivated_drop_down_option)

    @allure.step
    def verify_create_new_not_displayed(self):
        assert self.btn_create_new_btn not in self.tag_name

    @allure.step
    def verify_first_campaign_in_list_view_detail(self, campaign_name, type):
        # generated_campaign_name = Form.generatedCampaignName[-1]
        self.hard_sleep(5)
        campaign_name_in_list = self.campaign_name_in_list_xpath.format(campaign_name)
        exist = self.page_operation.element_exists((By.XPATH, campaign_name_in_list), 30)
        return exist

    @allure.step
    def search_and_verify_first_campaign_in_list_view(self, campaign_name, type):
        i = 0
        test_result = False
        while i <= 5 and (test_result is False):
            # self.click_search_btn()
            test_result = self.verify_first_campaign_in_list_view_detail(campaign_name, type)
            i = i + 1
        assert test_result is True, "Search campaign:{} fail.".format(Form.generatedCampaignName[-1])

    @allure.step
    def click_create_new_btn(self):
        self.hard_sleep(5)
        self.page_operation.click_element(self.btn_create_new_btn)
    
    @allure.step
    def go_to_create_page(self):
        self.page_operation.go_to_url("/rewards/create")
        retry = 4
        while retry > 0 and (not self.page_operation.element_visible(self.save_btn, timeout=30)):
            self.page_operation.go_to_url("/rewards/create")
            time.sleep(10)
            retry = retry - 1
        assert self.page_operation.element_visible(self.save_btn, timeout=15) is True, "go to create page fail"


    @allure.step
    def go_to_edit_page(self, campaign_id):
        self.page_operation.go_to_url("/edit/" + campaign_id)
        self.hard_sleep(10)

    @allure.step
    def wait_search_page_load(self):
        self.page_operation.element_visible(self.start_date_calendar)

    @allure.step
    def click_list_view_start_date_calendar(self):
        def until_condition():
            return self.page_operation.element_visible(self.year_calendar_drop_down,5)
        self.page_operation.click_element(self.start_date_calendar, until_condition)

    @allure.step
    def click_list_view_end_date_calendar(self):
        def until_condition():
            return self.page_operation.element_visible(self.year_calendar_drop_down, 5)
        self.page_operation.click_element(self.end_date_calendar, until_condition)

    @allure.step
    def click_search_btn(self):
        self.page_operation.click_element(self.btn_search)
        # self.hard_sleep(30)

    @allure.step
    def click_clear_btn(self):
        self.hard_sleep(10)
        self.page_operation.element_visible(self.btn_clear)
        self.page_operation.click_element(self.btn_clear)
        self.page_operation.element_visible(self.btn_clear)
        self.hard_sleep(20)

    @allure.step
    def click_first_campaign_in_list_view(self, campaign_name):
        # self.page_operation.click_element(self.first_campaign)
        self.page_operation.click_element((By.XPATH, self.campaign_name_in_list_xpath.format(campaign_name)))
        self.hard_sleep(5)

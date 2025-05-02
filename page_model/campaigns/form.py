__author__ = 'nogu'

from telnetlib import EC
import allure
from selenium.common.exceptions import TimeoutException
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from ui.base import Base
from datetime import date
from ui.support.generate_unique_name import GenerateUniqueName
from controls_v3.form_operation import FormOperation
import time
from utils import logger


class Form(Base):
    generatedCampaignName = []
    generatedRcode = []
    # header
    create_new_campaign_header_label_id_txt = (
    By.CSS_SELECTOR, 'span[data-qa-element="brm-campaigns-form-header-label-campaign-id"]')
    create_new_campaign_header_title_txt = (
    By.CSS_SELECTOR, 'span[data-qa-element="brm-campaigns-form-header-title-campaign"]')
    header_warning_message = (By.CSS_SELECTOR, 'div[data-qa-element="brm-campaigns-form-alert"]')
    # phoebe's test cases required
    phoebe_campaign_type_drop_down = (By.CSS_SELECTOR, "div[data-qa-element='bui-value-wrapper']")
    phoebe_item_level_campaign_type_option = (By.CSS_SELECTOR,
                                              "div[data-qa-element='brm-campaigns-search-criteria-drop-down-list-campaign-type'] div[data-qa-element='bui-option-list'] div[data-qa-element='bui-option-item-1']")
    phoebe_order_level_campaign_type_option = (By.CSS_SELECTOR,
                                               "div[data-qa-element='brm-campaigns-search-criteria-drop-down-list-campaign-type'] div[data-qa-element='bui-option-list'] div[data-qa-element='bui-option-item-2']")
    phoebe_search_button = (By.CSS_SELECTOR, "button[data-qa-element='brm-campaigns-search-criteria-button-search']")
    phoebe_campaign_id = (By.CSS_SELECTOR, "div[data-qa-element='brm-campaigns-list-card-data-column-2']")
    phoebe_first_campaign = (By.CSS_SELECTOR, "div[data-qa-element='brm-campaigns-list-card-data-row-0']")
    phoebe_first_campaign_name = (By.CSS_SELECTOR, "div[data-qa-element='brm-campaigns-list-card-data-column-2']")
    phoebe_first_campaign_status = (By.CSS_SELECTOR, "div[data-qa-element='brm-campaigns-list-card-data-column-3']")
    phoebe_first_campaign_creater = (By.CSS_SELECTOR, "span[data-qa-element='brm-campaigns-form-header-span-created']")
    phoebe_rewards_campaign_link = (By.CSS_SELECTOR, "a[data-qa-element='bui-crumb-0']")
    # type
    campaign_type_drop_down = (
    By.CSS_SELECTOR, 'div[data-qa-element="brm-campaigns-form-detail-drop-down-list-campaign-type"]')
    order_level_campaign_type_option = (By.CSS_SELECTOR,
                                        'div[data-qa-element="brm-campaigns-form-detail-drop-down-list-campaign-type"] div[data-qa-element="bui-option-list"] div[data-qa-element="bui-option-item-0"]')
    item_level_campaign_type_option = (By.CSS_SELECTOR,
                                       'div[data-qa-element="brm-campaigns-form-detail-drop-down-list-campaign-type"] div[data-qa-element="bui-option-list"] div[data-qa-element="bui-option-item-1"]')
    rcode_order_level_campaign_type_option = (By.CSS_SELECTOR,
                                              'div[data-qa-element="brm-campaigns-form-detail-drop-down-list-campaign-type"] div[data-qa-element="bui-option-list"] div[data-qa-element="bui-option-item-2"]')
    rcode_item_level_campaign_type_option = (By.CSS_SELECTOR,
                                             'div[data-qa-element="brm-campaigns-form-detail-drop-down-list-campaign-type"] div[data-qa-element="bui-option-list"] div[data-qa-element="bui-option-item-3"]')
    shipping_credit_campaign_type_option = (By.CSS_SELECTOR,
                                            'div[data-qa-element="brm-campaigns-form-detail-drop-down-list-campaign-type"] div[data-qa-element="bui-option-list"] div[data-qa-element="bui-option-item-4"]')
    rcode_shipping_credit_campaign_type_option = (By.CSS_SELECTOR,
                                                  'div[data-qa-element="brm-campaigns-form-detail-drop-down-list-campaign-type"] div[data-qa-element="bui-option-list"] div[data-qa-element="bui-option-item-5"]')
    # name
    campaign_name_warning_message = (By.CSS_SELECTOR, 'div[data-qa-element="bui-error-message"]')
    campaign_name_input = (
    By.CSS_SELECTOR, 'div[data-qa-element="brm-campaigns-form-detail-text-box-campaign-name"] input')
    # date range
    date_range_warning_message = (
    By.CSS_SELECTOR, 'div[data-qa-element="brm-campaigns-form-detail-div-date-range-error-msg"]')
    date_range_always_active_radio_btn = (
    By.CSS_SELECTOR, 'div[data-qa-element="brm-campaigns-form-detail-switch-button-is-always-active"]')
    start_date_txt_box = (By.CSS_SELECTOR,
                          'div[data-qa-element="brm-campaigns-form-detail-date-picker-date-range-start-date"] div[data-qa-element="bui-textbox"] div input[data-qa-element="bui-textbox-input"]')
    right_arrow_in_calendar = (By.CSS_SELECTOR, 'svg[data-qa-element="bui-arrow-right-icon"]')
    end_date_txt_box = (By.CSS_SELECTOR,
                        'div[data-qa-element="brm-campaigns-form-detail-date-picker-date-range-end-date"] div[data-qa-element="bui-textbox"] div input[data-qa-element="bui-textbox-input"]')
    dates_calendar = (By.CSS_SELECTOR, 'div[data-qa-calendar-item]')
    year_calendar_drop_down = (By.CSS_SELECTOR, 'div[data-qa-element="bui-year-dropdown"]')
    year_calendar_option = (
    By.CSS_SELECTOR, 'div[data-qa-element="bui-year-dropdown"] div div div[class="css-17393pb"] div')
    start_hour_drop_down = (
    By.CSS_SELECTOR, 'div[data-qa-element="brm-campaigns-form-detail-drop-down-list-date-range-start-hour"]')
    start_hour_option = (By.CSS_SELECTOR,
                         'div[data-qa-element="brm-campaigns-form-detail-drop-down-list-date-range-start-hour"] div[data-qa-element="bui-option-list"] div[data-qa-element="bui-option-item-9"]')
    end_hour_drop_down = (
    By.CSS_SELECTOR, 'div[data-qa-element="brm-campaigns-form-detail-drop-down-list-date-range-end-hour"]')
    end_hour_option = (By.CSS_SELECTOR,
                       'div[data-qa-element="brm-campaigns-form-detail-drop-down-list-date-range-end-hour"] div[data-qa-element="bui-option-list"] div[data-qa-element="bui-option-item-23"]')
    # store
    iherb_store_chk_box = (By.CSS_SELECTOR, 'div[data-qa-element="brm-campaigns-form-detail-checkbox-store-iherb"]')
    love_letter_store_chk_box = (
    By.CSS_SELECTOR, 'div[data-qa-element="brm-campaigns-form-detail-checkbox-store-love-letter"]')
    # platforms
    all_platforms_toggle_btn = (
    By.CSS_SELECTOR, 'div[data-qa-element="brm-campaigns-form-detail-switch-button-is-all-platform"]')
    desktop_platform_chk_box = (By.CSS_SELECTOR, 'div[data-qa-element="brm-campaigns-form-detail-checkbox-desktop"]')
    mobile_platform_chk_box = (By.CSS_SELECTOR, 'div[data-qa-element="brm-campaigns-form-detail-checkbox-mobile"]')
    android_global_platform_chk_box = (
    By.CSS_SELECTOR, 'div[data-qa-element="brm-campaigns-form-detail-checkbox-android-global"]')
    iphone_global_platform_chk_box = (
    By.CSS_SELECTOR, 'div[data-qa-element="brm-campaigns-form-detail-checkbox-iphone-global"]')
    android_china_platform_chk_box = (
    By.CSS_SELECTOR, 'div[data-qa-element="brm-campaigns-form-detail-checkbox-android-china"]')
    iphone_china_platform_chk_box = (
    By.CSS_SELECTOR, 'div[data-qa-element="brm-campaigns-form-detail-checkbox-iphone-china"]')
    wechat_mini_china_platform_chk_box = (
    By.CSS_SELECTOR, 'div[data-qa-element="brm-campaigns-form-detail-checkbox-wechatmini"]')
    # countries
    countries_warning_message = (
    By.CSS_SELECTOR, 'div[data-qa-element="brm-campaigns-form-detail-div-countries-error-msg"]')
    all_countries_radio_btn = (
    By.CSS_SELECTOR, 'div[data-qa-element="brm-campaigns-form-detail-switch-button-is-all-countries"]')
    search_countries_input = (
    By.CSS_SELECTOR, 'div[data-qa-element="brm-campaigns-form-detail-auto-suggestion-countries"] input')
    select_country_option = (By.CSS_SELECTOR,
                             'div[data-qa-element="brm-campaigns-form-detail-auto-suggestion-countries"] div[data-qa-element="bui-result-list"] div[data-qa-element="bui-result-item-0"]')
    # referral codes
    r_codes_warning_message = (
    By.CSS_SELECTOR, 'div div[data-qa-element="brm-campaigns-form-detail-div-referral-codes-error-msg"]')
    all_r_codes_radio_btn = (
    By.CSS_SELECTOR, 'div[data-qa-element="brm-campaigns-form-detail-switch-button-is-all-referral-codes"]')
    search_r_codes_input = (
    By.CSS_SELECTOR, 'div[data-qa-element="brm-campaigns-form-detail-auto-suggestion-referral-codes"] input')
    select_r_code_option = (By.CSS_SELECTOR,
                            'div[data-qa-element="brm-campaigns-form-detail-auto-suggestion-referral-codes"] div[data-qa-element="bui-result-list"] div[data-qa-element="bui-result-item-0"]')
    r_code_add_btn = (By.CSS_SELECTOR, 'button[data-qa-element="brm-campaigns-form-detail-button-add-referral-codes"]')
    # shipping services
    shipping_services_warning_message = (
    By.CSS_SELECTOR, 'div[data-qa-element="brm-campaigns-form-detail-div-shipping-services-error-msg"]')
    all_shipping_services_btn = (
    By.CSS_SELECTOR, 'div[data-qa-element="brm-campaigns-form-detail-switch-button-is-all-shipping-services"]')
    search_shipping_services_input = (By.CSS_SELECTOR, 'input[placeholder="Search Shipping Services"]')
    select_shipping_services_option = (By.CSS_SELECTOR,
                                       'div[data-qa-element="brm-campaigns-form-detail-auto-suggestion-shipping-services"] div[data-qa-element="bui-result-list"] div[data-qa-element="bui-result-item-0"]')
    # item-level
    products_warning_message = (
    By.CSS_SELECTOR, 'div[data-qa-element="brm-campaigns-form-detail-div-products-error-msg"]')
    brands_warning_message = (By.CSS_SELECTOR, 'div[data-qa-element="brm-campaigns-form-detail-div-brands-error-msg"]')
    order_level_chk_box = (
    By.CSS_SELECTOR, 'div[data-qa-element="brm-campaigns-form-detail-radio-button-promotion-level-order-level"]')
    item_level_chk_box = (
    By.CSS_SELECTOR, 'div[data-qa-element="brm-campaigns-form-detail-radio-button-promotion-level-item-level"]')
    search_products_input = (
    By.CSS_SELECTOR, 'div[data-qa-element="brm-campaigns-form-detail-auto-suggestion-products"] input')
    select_product_option = (By.CSS_SELECTOR,
                             'div[data-qa-element="brm-campaigns-form-detail-auto-suggestion-products"] div[data-qa-element="bui-result-list"] div[data-qa-element="bui-result-item-0"]')
    search_brands_input = (
    By.CSS_SELECTOR, 'div[data-qa-element="brm-campaigns-form-detail-auto-suggestion-brands"] input')
    select_brand_option = (By.CSS_SELECTOR,
                           'div[data-qa-element="brm-campaigns-form-detail-auto-suggestion-brands"] div[data-qa-element="bui-result-list"] div[data-qa-element="bui-result-item-0"]')
    # rebate setting
    add_at_least_one_discount_or_commission_warning_message = (
    By.CSS_SELECTOR, 'div[data-qa-element="brm-campaigns-form-div-rebate-setting-error-msg"]')
    discount_new_customers_chk_box = (
    By.CSS_SELECTOR, 'div[data-qa-element="brm-campaigns-form-rebate-setting-checkbox-discount-for-new-customer"]')
    discount_new_customers_value_input = (By.CSS_SELECTOR,
                                          'div[data-qa-element="brm-campaigns-form-rebate-setting-text-box-discount-for-new-customer-value"] input')
    discount_new_customers_min_order_amount_input = (By.CSS_SELECTOR,
                                                     'div[data-qa-element="brm-campaigns-form-rebate-setting-text-box-discount-for-new-customer-min-order-amount"] input')
    discount_existing_customers_chk_box = (
    By.CSS_SELECTOR, 'div[data-qa-element="brm-campaigns-form-rebate-setting-checkbox-discount-for-existing-customer"]')
    discount_existing_customers_value_input = (By.CSS_SELECTOR,
                                               'div[data-qa-element="brm-campaigns-form-rebate-setting-text-box-discount-for-existing-customer-value"] input')
    discount_existing_customers_min_order_amount_input = (By.CSS_SELECTOR,
                                                          'div[data-qa-element="brm-campaigns-form-rebate-setting-text-box-discount-for-existing-customer-min-order-amount"] input')
    commission_new_customers_chk_box = (
    By.CSS_SELECTOR, 'div[data-qa-element="brm-campaigns-form-rebate-setting-checkbox-commission-for-new-customer"]')
    commission_new_customers_value_input = (By.CSS_SELECTOR,
                                            'div[data-qa-element="brm-campaigns-form-rebate-setting-text-box-commission-for-new-customer-value"] input')
    commission_existing_customers_chk_box = (By.CSS_SELECTOR,
                                             'div[data-qa-element="brm-campaigns-form-rebate-setting-checkbox-commission-for-existing-customer"]')
    commission_existing_customers_value_input = (By.CSS_SELECTOR,
                                                 'div[data-qa-element="brm-campaigns-form-rebate-setting-text-box-commission-for-existing-customer-value"] input')
    shipping_credit_new_customers_chk_box = (
    By.CSS_SELECTOR, 'div[data-qa-element="brm-campaigns-form-rebate-setting-checkbox-discount-for-new-customer"]')
    shipping_credit_new_customers_value_input = (By.CSS_SELECTOR,
                                                 'div[data-qa-element="brm-campaigns-form-rebate-setting-text-box-discount-for-new-customer-value"] div input')
    shipping_credit_existing_customers_chk_box = (
    By.CSS_SELECTOR, 'div[data-qa-element="brm-campaigns-form-rebate-setting-checkbox-discount-for-existing-customer"]')
    shipping_credit_existing_customers_value_input = (By.CSS_SELECTOR,
                                                      'div[data-qa-element="brm-campaigns-form-rebate-setting-text-box-discount-for-existing-customer-value"] div input')
    discount_limit = (
    By.CSS_SELECTOR, 'div[data-qa-element="brm-campaigns-form-detail-switch-button-is-no-discount-redemption-limit"]')
    commission_limit = (
    By.CSS_SELECTOR, 'div[data-qa-element="brm-campaigns-form-detail-switch-button-is-no-commission-redemption-limit"]')
    discount_limit_input = (
    By.CSS_SELECTOR, 'div[data-qa-element="brm-campaigns-form-detail-text-box-discount-redemption-limit"] div input')
    commission_limit_input = (
    By.CSS_SELECTOR, 'div[data-qa-element="brm-campaigns-form-detail-text-box-commission-redemption-limit"] div input')
    # buttons
    modal_confirm_btn = (By.CSS_SELECTOR, 'button[data-qa-element="brm-campaigns-confirm-modal-button-confirm"]')
    modal_cancel_btn = (By.CSS_SELECTOR, 'button[data-qa-element="brm-campaigns-confirm-modal-button-cancel"]')
    save_btn = (By.CSS_SELECTOR, 'button[data-qa-element="brm-campaigns-form-header-button-save"]')
    cancel_btn = (By.CSS_SELECTOR, 'button[data-qa-element="brm-campaigns-form-header-button-cancel"]')
    deactivated_txt = (By.XPATH, '//span[text()="Deactivated"]')
    deactivate_btn = (By.CSS_SELECTOR, 'button[data-qa-element="brm-campaigns-form-header-button-deactivate"]')
    approve_btn = (By.CSS_SELECTOR, 'button[data-qa-element="brm-campaigns-form-header-button-approve"]')
    tag_name = (By.TAG_NAME, 'body')
    # input
    search_countries_and_names_input = (
    By.CSS_SELECTOR, 'div[data-qa-element="brm-campaigns-search-criteria-auto-suggestion-search"] input')
    # select
    exclude_country_hk = (By.CSS_SELECTOR,
                          'div[data-qa-element="brm-selected-options"] select[data-qa-element="brm-select"] option[value="HK"]')
    exclude_country_kr = (By.CSS_SELECTOR,
                          'div[data-qa-element="brm-selected-options"] select[data-qa-element="brm-select"] option[value="KR"]')
    exclude_country_ru = (By.CSS_SELECTOR,
                          'div[data-qa-element="brm-selected-options"] select[data-qa-element="brm-select"] option[value="RU"]')
    select_all_country = (By.CSS_SELECTOR, 'button[data-qa-element="brm-move-all-to-selected-button"]')
    exclude_button = (By.CSS_SELECTOR, 'button[data-qa-element="brm-move-to-unselected-button"]')
    # camref
    save_camref_button = (By.CSS_SELECTOR, 'button[data-qa-element="brm-campaigns-confirm-modal-button-confirm"]')
    load_image = (By.XPATH, "//*[name()='path' and @d='M0 0h192v192H0z']")
    pagination_1 = (By.XPATH, '//div[@data-qa-element="bui-page-item-1"]')
    default_check_element_exist_time_out = 1
    first_campaign_name_text = (By.XPATH, '//div[@data-qa-element="brm-campaigns-list-card-data-row-0"]/div[3]')
    first_campaign_row = (By.XPATH, '//div[@data-qa-element="brm-campaigns-list-card-data-row-0"]')
    rcode_tab = (By.CSS_SELECTOR, 'div[data-qa-element="bui-label-item-1"]')
    country_al = (By.CSS_SELECTOR,
                  'div[data-qa-element="brm-unselected-options"] select[data-qa-element="brm-select"] option[value="AL"]')
    include_button = (By.CSS_SELECTOR, 'button[data-qa-element="brm-move-to-selected-button"]')
    country_dz = (By.CSS_SELECTOR,
                  'div[data-qa-element="brm-unselected-options"] select[data-qa-element="brm-select"] option[value="DZ"]')

    @allure.step
    def verify_create_new_campaign_header_title_txt(self):
        self.page_operation.assert_element_exist(self.create_new_campaign_header_title_txt)

    @allure.step
    def verify_header_warning_message(self):
        self.page_operation.assert_element_exist(self.header_warning_message)

    @allure.step
    def verify_add_at_least_one_discount_or_commission_warning_message(self):
        self.page_operation.assert_element_exist(self.add_at_least_one_discount_or_commission_warning_message)

    @allure.step
    def verify_name_warning_message(self):
        self.page_operation.assert_element_exist(self.campaign_name_warning_message)

    @allure.step
    def verify_date_range_warning_message(self):
        self.page_operation.assert_element_exist(self.date_range_warning_message)

    @allure.step
    def verify_countries_warning_message(self):
        self.page_operation.assert_element_exist(self.countries_warning_message)

    @allure.step
    def verify_code_warning_message(self):
        self.page_operation.assert_element_exist(self.r_codes_warning_message)

    @allure.step
    def verify_shipping_services_warning_message(self):
        self.page_operation.assert_element_exist(self.shipping_services_warning_message)

    @allure.step
    def wait_campaign_type_drop_down(self):
        self.page_operation.element_visible(self.campaign_type_drop_down, 3)

    @allure.step
    def click_campaign_type_drop_down(self):
        self.page_operation.click_element(self.campaign_type_drop_down)
        self.hard_sleep(10)

    @allure.step
    def click_order_level_campaign_type_option(self):
        self.hard_sleep(5)
        # self.page_operation.click_element(self.order_level_campaign_type_option)
        FormOperation(self.context, self.page_operation).click_drop_down_menu(self.campaign_type_drop_down,
                                                                              self.order_level_campaign_type_option)

    @allure.step
    def click_item_level_campaign_type_option(self):
        FormOperation(self.context, self.page_operation).click_drop_down_menu(self.campaign_type_drop_down,
                                                                              self.item_level_campaign_type_option)

    @allure.step
    def click_rcode_order_level_campaign_type_option(self):
        FormOperation(self.context, self.page_operation).click_drop_down_menu(self.campaign_type_drop_down,
                                                                              self.rcode_order_level_campaign_type_option)
        # self.page_operation.click_element(self.rcode_order_level_campaign_type_option)

    @allure.step
    def click_rcode_item_level_campaign_type_option(self):
        # self.page_operation.click_element(self.rcode_item_level_campaign_type_option)
        FormOperation(self.context, self.page_operation).click_drop_down_menu(self.campaign_type_drop_down,
                                                                              self.rcode_item_level_campaign_type_option)

    @allure.step
    def click_shipping_credit_campaign_type_option(self):
        FormOperation(self.context, self.page_operation).click_drop_down_menu(self.campaign_type_drop_down,
                                                                              self.shipping_credit_campaign_type_option)

    @allure.step
    def click_rcode_shipping_credit_campaign_type_option(self):
        FormOperation(self.context, self.page_operation).click_drop_down_menu(self.campaign_type_drop_down,
                                                                              self.rcode_shipping_credit_campaign_type_option)
        # self.page_operation.click_element(self.rcode_shipping_credit_campaign_type_option)

    @allure.step
    def enter_campaign_name(self):
        time.sleep(3)
        campaign_name = 'T' + GenerateUniqueName().get_snap_shot()
        self.generatedCampaignName.append(campaign_name)
        self.page_operation.find_element(self.campaign_name_input).clear()
        time.sleep(3)
        self.page_operation.input_element(self.campaign_name_input, campaign_name)
        logger.info('set campaign name: ' + campaign_name)
        return campaign_name

    @allure.step
    def enter_updated_campaign_name(self):
        updated_campaign_name = 'Phoebe' + GenerateUniqueName().get_snap_shot()
        self.generatedCampaignName.append(updated_campaign_name)
        self.page_operation.find_element(self.campaign_name_input).clear()
        time.sleep(3)
        self.page_operation.input_element(self.campaign_name_input, updated_campaign_name)
        logger.info('set campaign name: ' + updated_campaign_name)
        return updated_campaign_name

    @allure.step
    def click_always_active_radio_btn(self):
        self.page_operation.click_element(self.date_range_always_active_radio_btn)

    @allure.step
    def click_start_date_calendar(self):
        self.page_operation.click_element(self.start_date_txt_box)
        self.hard_sleep(5)

    @allure.step
    def click_right_arrow_in_calendar(self):
        self.page_operation.click_element(self.right_arrow_in_calendar)

    @allure.step
    def click_end_date_calendar(self):
        self.page_operation.click_element(self.end_date_txt_box)

    @allure.step
    def select_today_date_from_calendar(self):
        self.page_operation.click_element(self.year_calendar_drop_down)
        system_year = int(date.today().strftime('%Y'))
        get_calendar_years = self.page_operation.find_elements(self.year_calendar_option)
        for span in get_calendar_years:
            if span.text.isdigit():
                get_calendar_date = int(span.text)
                if get_calendar_date == system_year + 1:
                    span.click()
                    break
        if not hasattr(self.context, 'campaign_create_date'):
            system_date = int(date.today().strftime('%d'))
            self.context.campaign_create_date = system_date
        else:
            system_date = self.context.campaign_create_date
        get_calendar_dates = self.page_operation.find_elements(self.dates_calendar)
        for span in get_calendar_dates:
            if span.text.isdigit():
                get_calendar_date = int(span.text)
                if get_calendar_date == system_date:
                    span.click()
                    break

    @allure.step
    def click_start_hour_drop_down(self):
        self.page_operation.click_element(self.start_hour_drop_down)

    @allure.step
    def select_start_hour_option(self):
        self.page_operation.click_element(self.start_hour_option)

    @allure.step
    def click_end_hour_drop_down(self):
        self.page_operation.click_element(self.end_hour_drop_down)

    @allure.step
    def select_end_hour_option(self):
        self.page_operation.click_element(self.end_hour_option)

    @allure.step
    def select_platform(self, platform):
        platform_text = By.CSS_SELECTOR, 'div[data-qa-element="brm-campaigns-form-detail-checkbox-' + platform + '"]'
        self.page_operation.click_element(platform_text)

    @allure.step
    def click_all_countries_radio_btn(self):
        self.page_operation.click_element(self.all_countries_radio_btn)

    @allure.step
    def select_country(self, country):
        self.page_operation.input_element(self.search_countries_input, country)
        self.hard_sleep(15)
        self.page_operation.click_element(self.select_country_option)

    @allure.step
    def exclude_country(self):
        self.page_operation.click_element(self.country_al)
        self.page_operation.click_element(self.country_dz)
        self.page_operation.click_element(self.include_button)

    @allure.step
    def many_country(self):
        self.page_operation.click_element(self.select_all_country)
        self.page_operation.click_element(self.exclude_country_hk)
        self.page_operation.click_element(self.exclude_button)
        self.page_operation.click_element(self.exclude_country_kr)
        self.page_operation.click_element(self.exclude_button)
        self.page_operation.click_element(self.exclude_country_ru)
        self.page_operation.click_element(self.exclude_button)

    @allure.step
    def select_code(self, code):
        self.page_operation.input_element(self.search_r_codes_input, code)
        self.generatedRcode.append(code)
        self.hard_sleep(15)
        # self.click_element(self.select_code_option)

    @allure.step
    def click_code_add_btn(self):
        self.page_operation.click_element(self.r_code_add_btn)

    @allure.step
    def click_all_shipping_services_radio_btn(self):
        self.page_operation.click_element(self.all_shipping_services_btn)

    @allure.step
    def click_order_level_chk_box(self):
        self.page_operation.click_element(self.order_level_chk_box)

    @allure.step
    def click_item_level_chk_box(self):
        self.page_operation.click_element(self.item_level_chk_box)

    @allure.step
    def select_products(self, products):
        self.page_operation.input_element(self.search_products_input, products)
        self.hard_sleep(10)
        self.page_operation.click_element(self.select_product_option)

    @allure.step
    def verify_products_warning_message(self):
        self.page_operation.assert_element_exist(self.products_warning_message)

    @allure.step
    def verify_brands_warning_message(self):
        self.page_operation.assert_element_exist(self.brands_warning_message)

    @allure.step
    def enter_limit_for_discount(self, dis_limit_num):
        self.page_operation.click_element(self.discount_limit)
        self.page_operation.input_element(self.discount_limit_input, dis_limit_num)

    @allure.step
    def enter_limit_for_commission(self, com_limit_num):
        self.page_operation.click_element(self.commission_limit)
        self.page_operation.input_element(self.commission_limit_input, com_limit_num)

    @allure.step
    def enter_new_customers_discount_value(self, dis_new_cus_val):
        self.page_operation.click_element(self.discount_new_customers_chk_box)
        discount_commission_value_options = (By.CSS_SELECTOR,
                                             'button[data-qa-element="brm-campaigns-form-rebate-setting-radio-button-group-discount-for-new-customer-type-percentage"]')
        self.page_operation.click_element(discount_commission_value_options)
        self.page_operation.input_element(self.discount_new_customers_value_input, dis_new_cus_val)

    @allure.step
    def enter_new_customers_min_order_value(self, dis_new_cus_min_order_val):
        self.page_operation.input_element(self.discount_new_customers_min_order_amount_input, dis_new_cus_min_order_val)

    @allure.step
    def enter_existing_customers_discount_value(self, dis_exist_cus_val):
        self.page_operation.click_element(self.discount_existing_customers_chk_box)
        discount_same_as_new_btn = (
        By.XPATH, '(.//*[normalize-space(text()) and normalize-space(.)="Discount Value"])[2]/preceding::button[1]')
        self.page_operation.click_element(discount_same_as_new_btn)
        self.page_operation.input_element(self.discount_existing_customers_value_input, dis_exist_cus_val)

    @allure.step
    def enter_existing_customers_min_order_value(self, dis_exist_cus_min_order_val):
        self.page_operation.input_element(self.discount_existing_customers_min_order_amount_input,
                                          dis_exist_cus_min_order_val)

    @allure.step
    def enter_new_customers_commission_value(self, commission_new_cus_val):
        self.page_operation.click_element(self.commission_new_customers_chk_box)
        discount_commission_value_options = (By.CSS_SELECTOR,
                                             'button[data-qa-element="brm-campaigns-form-rebate-setting-radio-button-group-commission-for-new-customer-type-percentage"]')
        self.page_operation.click_element(discount_commission_value_options)
        self.page_operation.input_element(self.commission_new_customers_value_input, commission_new_cus_val)

    @allure.step
    def enter_existing_customers_commission_value(self, commission_exist_cus_val):
        self.page_operation.click_element(self.commission_existing_customers_chk_box)
        commission_same_as_new_btn = (
        By.XPATH, '(.//*[normalize-space(text()) and normalize-space(.)="Commission Value"])[2]/preceding::button[1]')
        self.page_operation.click_element(commission_same_as_new_btn)
        self.page_operation.input_element(self.commission_existing_customers_value_input, commission_exist_cus_val)

    @allure.step
    def enter_new_customers_shipping_credit_value(self, shipping_new_cus_val):
        self.page_operation.click_element(self.shipping_credit_new_customers_chk_box)
        self.page_operation.input_element(self.shipping_credit_new_customers_value_input, shipping_new_cus_val)

    @allure.step
    def enter_existing_customers_shipping_credit_value(self, shipping_exist_cus_val):
        self.page_operation.click_element(self.shipping_credit_existing_customers_chk_box)
        shipping_credit_same_as_new_btn = (
        By.CSS_SELECTOR, 'button[data-qa-element="brm-campaigns-form-rebate-setting-button-same-as-new"]')
        self.page_operation.click_element(shipping_credit_same_as_new_btn)
        self.page_operation.input_element(self.shipping_credit_existing_customers_value_input, shipping_exist_cus_val)

    @allure.step
    def save_and_confirm_campaign(self):
        retry = 1
        confirm_successfully = False
        while (retry > 0) and (confirm_successfully is False):
            # cancel_button_exist = self.page_operation.element_visible(self.modal_cancel_btn, 2)
            # if cancel_button_exist:
            #     self.page_operation.click_element(self.modal_cancel_btn)
            confirm_successfully = self.click_save_and_confirm_btn()
            retry = retry - 1
        assert confirm_successfully is True, "confirm modal button fail."

    @allure.step
    def save_new_campaign(self):
        self.page_operation.press_page_up_button()
        self.page_operation.click_element(self.save_btn)
        try:
            self.page_operation.click_element(self.modal_confirm_btn)
            WebDriverWait(self.page_operation.driver, 60).until(
                EC.visibility_of_element_located(self.first_campaign_row))
        except TimeoutException:
            raise TimeoutException(
                'after save campaign and confirm 60s, campaign list page not loaded well so Element is not clickable')

    @allure.step
    def save_without_info(self):
        self.page_operation.click_element(self.save_btn)

    @allure.step
    def save_camref(self):
        self.page_operation.click_element(self.save_camref_button)
        time.sleep(3)

    @allure.step
    def click_modal_confirm_btn(self):
        confirm_button = self.page_operation.find_element(
            self.modal_confirm_btn,
            timeout=15
        )
        confirm_button.click()
        try:
            WebDriverWait(self.page_operation.driver, 90).until(
                EC.visibility_of_element_located(self.first_campaign_row))
        except TimeoutException:
            raise TimeoutException(
                'after clicking confirm button 90s, campaign list page not loaded well so Element is not clickable')

    @allure.step
    def click_cancel_btn(self):
        cancel_btn = self.page_operation.find_element(
            self.cancel_btn,
            timeout=15
        )
        cancel_btn.click()

    # @allure.step
    # def verify_first_campaign_in_list_view(self):
    #     generated_campaign_name = self.generatedCampaignName[-1]
    #     campaign_name_list_view = self.page_operation.get_text_element(self.list_container)
    #     return generated_campaign_name in campaign_name_list_view

    @allure.step
    def click_generated_campaign(self):
        self.page_operation.click_element(self.first_campaign)
        self.hard_sleep(7)

    @allure.step
    def verify_approve_btn_not_displayed(self):
        assert self.approve_btn not in self.tag_name

    @allure.step
    def click_approve_btn(self):
        self.page_operation.element_exists(self.approve_btn)
        self.page_operation.click_element(self.approve_btn)
        self.hard_sleep(10)

    # @allure.step
    # def click_modal_confirm_btn(self):
    #     retry = 5
    #     confirm_successfully = False
    #     while (retry >= 0) and (confirm_successfully is False):
    #         cancel_button_exist = self.page_operation.element_visible(self.modal_cancel_btn, 2)
    #         if cancel_button_exist:
    #             self.page_operation.click_element(self.modal_cancel_btn)
    #         confirm_successfully = self.click_modal_confirm_btn_step()
    #         retry = retry - 1
    #         time.sleep(5)
    #     assert confirm_successfully is True, "confirm modal buttom fail."

    @allure.step
    def click_save_and_confirm_btn(self):
        self.page_operation.click_element(self.save_btn)
        time.sleep(5)

        # confirm_button = self.page_operation.find_element(
        #     self.modal_confirm_btn,
        #     timeout=10
        # )
        # self.page_operation.mouse_hover_on_element(self.modal_confirm_btn)
        # confirm_button.click()
        self.page_operation.click_element(self.modal_confirm_btn)
        self.hard_sleep(20)
        # confirm_successfully = not (self.page_operation.element_exists(self.modal_confirm_btn, timeout=5))
        confirm_successfully = True
        return confirm_successfully

    @allure.step
    def verify_deactivate_btn_not_displayed(self):
        assert self.deactivate_btn not in self.tag_name

    @allure.step
    def verify_deactivate_btn_is_displayed(self):
        element = self.page_operation.find_element(
            self.deactivate_btn,
            timeout=10
        )
        self.page_operation.mouse_hover_on_element(element)
        assert self.page_operation.element_exists(self.deactivate_btn)
        self.hard_sleep(5)

    @allure.step
    def verify_deactivated_txt(self):
        assert self.page_operation.element_exists(self.deactivated_txt)

    @allure.step
    def click_deactivate_btn(self):
        self.page_operation.click_element(self.deactivate_btn)
        self.hard_sleep(3)
        # retry = 5
        # button_exist = False
        # while (retry >= 0) and (button_exist is False):
        #     self.context.browser.get_webdriver().refresh()
        #     time.sleep(30)
        #     button_exist = self.page_operation.element_visible(self.deactivate_btn)
        #
        # deactivate_button = self.page_operation.find_element(
        #     self.deactivate_btn,
        #     timeout=30
        # )
        # self.page_operation.mouse_hover_on_element(self.deactivate_btn)
        # deactivate_button.click()

    @allure.step
    def click_save_changes_btn(self):
        self.hard_sleep(2)
        self.page_operation.click_element(self.save_btn)

    @allure.step
    def get_campaign_id(self):
        return self.page_operation.get_text_element(self.create_new_campaign_header_label_id_txt, 10)

    @allure.step
    def get_first_campaign_name(self):
        self.hard_sleep(3)
        return self.page_operation.get_text_element(self.phoebe_first_campaign_name, 10)

    @allure.step
    def get_first_campaign_creater(self):
        return self.page_operation.get_text_element(self.phoebe_first_campaign_creater, 10)

    @allure.step
    def back_to_rewards_campaigns(self):
        self.page_operation.click_element(self.phoebe_rewards_campaign_link)

    @allure.step
    def click_phoebe_campaign_type_drop_down(self):
        self.page_operation.click_element(self.phoebe_campaign_type_drop_down)
        try:
            WebDriverWait(self.page_operation.driver, 10).until(
                EC.visibility_of_element_located(self.phoebe_item_level_campaign_type_option))
        except TimeoutException:
            raise TimeoutException(
                'after clicking type drop down 10s, drop down option not loaded well so Element is not clickable')

    @allure.step
    def click_phoebe_item_campaign_type_option(self):
        self.page_operation.click_element(self.phoebe_item_level_campaign_type_option)
        self.hard_sleep(10)

    @allure.step
    def click_phoebe_order_campaign_type_option(self):
        self.page_operation.click_element(self.phoebe_order_level_campaign_type_option)
        self.hard_sleep(10)

    @allure.step
    def click_phoebe_search_button(self):
        self.page_operation.click_element(self.phoebe_search_button)
        try:
            WebDriverWait(self.page_operation.driver, 10).until(
                EC.visibility_of_element_located(self.first_campaign_row))
        except TimeoutException:
            raise TimeoutException(
                'after clicking earch button 10s, campaign list page not loaded well so Element is not clickable')

    @allure.step
    def click_first_campaign_list(self):
        self.page_operation.click_element(self.phoebe_first_campaign)
        try:
            WebDriverWait(self.page_operation.driver, 30).until(
                EC.visibility_of_element_located(self.create_new_campaign_header_title_txt))
        except TimeoutException:
            raise TimeoutException(
                'after clicking first campaign 30s, campaign detailed page not loaded well so Element is not clickable')

    # @allure.step
    # def check_correct_deactive_campaign(self, updated_campaign_name):
    #     assert self.page_operation.find_element(self.first_campaign_name_text).text == updated_campaign_name

    @allure.step
    def search_first_item_level_campaign(self, campaign_name):
        if self.page_operation.element_exists(self.search_countries_and_names_input, 5):
            self.page_operation.input_element(self.search_countries_and_names_input, campaign_name)

    @allure.step
    def verify_campaign_status(self):
        campain_status = self.page_operation.get_text_element(self.phoebe_first_campaign_status)
        if campain_status == "Deactivated":
            logger.info("deactivate successfully")
        else:
            logger.info("the status is" + campain_status)

    @allure.step
    def input_new_campaign_name(self, new_campaign_name):
        self.page_operation.input_element(self.campaign_name_input, new_campaign_name)

    @allure.step
    def click_rcode_tab(self):
        self.page_operation.click_element((self.rcode_tab))
        self.hard_sleep(10)

    @allure.step
    def click_campaign_which_I_want(self, campaign_name):
        campaign_which_want_in_list = (By.XPATH, '//div[contains(text(),"' + campaign_name + '")]')
        try:
            WebDriverWait(self.page_operation.driver, 30).until(
                EC.visibility_of_element_located(campaign_which_want_in_list))
        except TimeoutException:
            raise TimeoutException('campaign list page not found this new created campaign')
        try:
            self.page_operation.click_element(campaign_which_want_in_list)
            WebDriverWait(self.page_operation.driver, 30).until(
                EC.visibility_of_element_located(self.create_new_campaign_header_title_txt))
        except TimeoutException:
            raise TimeoutException(
                'after clicking campaign which I want 30s, campaign detailed page not loaded well so Element is not clickable')

__author__ = 'nogu'

from behave import given, when, then
from page_model.campaigns.list import List
from page_model.campaigns.form import Form
from features.fixture_context import BehavePatcher
import time
from utils import logger


@given('open baidu page')
def step_impl(context):
    context.browser.open("www.baidu.com")


@given('I can go to the create page')
def step_impl(context):
    context.rewards_campaign_list_page = List(context)
    context.rewards_campaign_list_page.go_to_create_page()


@given('I search first item level campaign')
def step_impl(context):
    context.rewards_campaign_form_page = Form(context)
    context.rewards_campaign_list_page = List(context)
    context.rewards_campaign_form_page.click_phoebe_campaign_type_drop_down()
    context.rewards_campaign_form_page.click_phoebe_item_campaign_type_option()
    context.rewards_campaign_form_page.click_phoebe_search_button()


@given('I search first item level campaign after update')
def step_impl(context):
    context.rewards_campaign_form_page = Form(context)
    context.rewards_campaign_list_page = List(context)
    context.rewards_campaign_form_page.click_phoebe_campaign_type_drop_down()
    context.rewards_campaign_form_page.click_phoebe_order_campaign_type_option()
    context.rewards_campaign_form_page.click_phoebe_order_campaign_type_option()
    context.rewards_campaign_form_page.click_phoebe_search_button()


@given('I search first order level campaign')
def step_impl(context):
    context.rewards_campaign_form_page = Form(context)
    context.rewards_campaign_form_page.click_phoebe_campaign_type_drop_down()
    context.rewards_campaign_form_page.click_phoebe_order_campaign_type_option()
    context.rewards_campaign_form_page.click_phoebe_search_button()


@given('I search first r-code item level campaign')
def step_impl(context):
    context.rewards_campaign_list_page = List(context)
    context.rewards_campaign_list_page.click_list_view_r_code_tab()
    context.rewards_campaign_form_page = Form(context)
    context.rewards_campaign_form_page.click_phoebe_campaign_type_drop_down()
    context.rewards_campaign_form_page.click_phoebe_item_campaign_type_option()
    context.rewards_campaign_form_page.click_phoebe_search_button()


@given('I search first r-code order level campaign')
def step_impl(context):
    context.rewards_campaign_list_page = List(context)
    context.rewards_campaign_list_page.click_list_view_r_code_tab()
    context.rewards_campaign_form_page = Form(context)
    context.rewards_campaign_form_page.click_phoebe_campaign_type_drop_down()
    context.rewards_campaign_form_page.click_phoebe_order_campaign_type_option()
    context.rewards_campaign_form_page.click_phoebe_search_button()


@then('I deactivate the created campaign in list')
def step_impl(context):
    context.rewards_campaign_form_page = Form(context)
    context.rewards_campaign_form_page.click_deactivate_btn()
    context.rewards_campaign_form_page.click_modal_confirm_btn()


@then('I update the campaign in list')
def step_impl(context):
    context.rewards_campaign_form_page = Form(context)
    context.updated_campaign_name = enter_updated_campaign_name(context)
    context.rewards_campaign_form_page.click_save_changes_btn()
    context.rewards_campaign_form_page.click_modal_confirm_btn()
    context.updated_campaign_name_in_list = context.rewards_campaign_form_page.get_first_campaign_name()
    if context.updated_campaign_name_in_list == context.updated_campaign_name:
        logger.info("updated successfully")
    else:
        logger.info("updated failed")
    context.rewards_campaign_form_page.click_first_campaign_list()
    context.creater = context.rewards_campaign_form_page.get_first_campaign_creater()
    context.original_creater = 'test-brm.campign-edi'
    if context.original_creater in context.creater:
        logger.info(context.creater + " is right")
    else:
        logger.info(context.creater)
    context.rewards_campaign_form_page.back_to_rewards_campaigns()


@then('I update the campaign in rcode list')
def step_impl(context):
    context.rewards_campaign_form_page = Form(context)
    context.updated_campaign_name = enter_updated_campaign_name(context)
    context.rewards_campaign_form_page.click_save_changes_btn()
    context.rewards_campaign_form_page.click_modal_confirm_btn()
    context.updated_campaign_name_in_list = context.rewards_campaign_form_page.get_first_campaign_name()
    if context.updated_campaign_name_in_list == context.updated_campaign_name:
        logger.info("updated successfully")
    else:
        logger.info("updated failed")


@then('Verify the first campaign in archived tab')
def stem_impl(context):
    context.rewards_campaign_list_page = List(context)
    context.rewards_campaign_list_page.click_list_view_archived_tab()
    context.rewards_campaign_form_page.search_first_item_level_campaign(context.campaign_name_created)
    context.rewards_campaign_form_page.click_phoebe_search_button()
    context.rewards_campaign_form_page.verify_campaign_status()


@when('click on the submit button without entering mandatory details for an order-level campaign')
def step_impl(context):
    context.rewards_campaign_form_page = Form(context)
    # context.rewards_campaign_form_page.click_campaign_type_drop_down()
    context.rewards_campaign_form_page.click_order_level_campaign_type_option()
    context.rewards_campaign_form_page.save_without_info()


@when('click on the submit button without entering mandatory details for an item-level campaign')
def step_impl(context):
    context.rewards_campaign_form_page = Form(context)
    # context.rewards_campaign_form_page.click_campaign_type_drop_down()
    context.rewards_campaign_form_page.click_item_level_campaign_type_option()
    context.rewards_campaign_form_page.save_without_info()


@when('click on the submit button without entering mandatory details for a rcode-order-level campaign')
def step_impl(context):
    context.rewards_campaign_form_page = Form(context)
    # context.rewards_campaign_form_page.click_campaign_type_drop_down()
    context.rewards_campaign_form_page.click_rcode_order_level_campaign_type_option()
    context.rewards_campaign_form_page.save_without_info()


@when('click on the submit button without entering mandatory details for a rcode-item-level campaign')
def step_impl(context):
    context.rewards_campaign_form_page = Form(context)
    # context.rewards_campaign_form_page.click_campaign_type_drop_down()
    context.rewards_campaign_form_page.click_rcode_item_level_campaign_type_option()
    context.rewards_campaign_form_page.save_without_info()


@when('click on the submit button without entering mandatory details for a shipping-credit campaign')
def step_impl(context):
    context.rewards_campaign_form_page = Form(context)
    context.rewards_campaign_form_page.click_campaign_type_drop_down()
    context.rewards_campaign_form_page.click_shipping_credit_campaign_type_option()
    context.rewards_campaign_form_page.save_without_info()


@when('click on the submit button without entering mandatory details for a rcode-shipping-credit campaign')
def step_impl(context):
    context.rewards_campaign_form_page = Form(context)
    context.rewards_campaign_form_page.click_campaign_type_drop_down()
    context.rewards_campaign_form_page.click_shipping_credit_campaign_type_option()
    context.rewards_campaign_form_page.save_without_info()


@when('click on the submit button without entering mandatory details for camref mapping')
def step_impl(context):
    context.rewards_campaign_form_page = Form(context)
    context.rewards_campaign_form_page.save_camref()


#


@then('I can see the order-level warning messages at header')
def step_impl(context):
    context.rewards_campaign_form_page.verify_create_new_campaign_header_title_txt()
    context.rewards_campaign_form_page.verify_header_warning_message()
    context.rewards_campaign_form_page.verify_name_warning_message()
    context.rewards_campaign_form_page.verify_date_range_warning_message()
    # context.rewards_campaign_form_page.verify_countries_warning_message()
    context.rewards_campaign_form_page.verify_add_at_least_one_discount_or_commission_warning_message()
    context.execute_steps(u"""
                  then I can cancel the campaign""")


@then('I can see the rcode-order-level warning messages at header')
def step_impl(context):
    context.rewards_campaign_form_page.verify_create_new_campaign_header_title_txt()
    context.rewards_campaign_form_page.verify_header_warning_message()
    # context.rewards_campaign_form_page.verify_name_warning_message()
    context.rewards_campaign_form_page.verify_date_range_warning_message()
    # context.rewards_campaign_form_page.verify_countries_warning_message()
    context.rewards_campaign_form_page.verify_add_at_least_one_discount_or_commission_warning_message()
    context.execute_steps(u"""
                      then I can cancel the campaign""")


@then('I can see the rcode-item-level warning messages at header')
def step_impl(context):
    context.rewards_campaign_form_page.verify_create_new_campaign_header_title_txt()
    context.rewards_campaign_form_page.verify_header_warning_message()
    # context.rewards_campaign_form_page.verify_name_warning_message()
    context.rewards_campaign_form_page.verify_date_range_warning_message()
    # context.rewards_campaign_form_page.verify_countries_warning_message()
    context.rewards_campaign_form_page.verify_add_at_least_one_discount_or_commission_warning_message()
    context.rewards_campaign_form_page.verify_products_warning_message()
    context.execute_steps(u"""
                      then I can cancel the campaign""")


@then('I can see the shipping-credit warning messages at header')
def step_impl(context):
    context.rewards_campaign_form_page.verify_create_new_campaign_header_title_txt()
    context.rewards_campaign_form_page.verify_header_warning_message()
    # context.rewards_campaign_form_page.verify_name_warning_message()
    context.rewards_campaign_form_page.verify_date_range_warning_message()
    context.rewards_campaign_form_page.verify_countries_warning_message()
    context.rewards_campaign_form_page.verify_shipping_services_warning_message()
    context.rewards_campaign_form_page.verify_add_at_least_one_discount_or_commission_warning_message()
    context.execute_steps(u"""
                      then I can cancel the campaign""")


@then('I can see the rcode-shipping-credit warning messages at header')
def step_impl(context):
    context.rewards_campaign_form_page.verify_create_new_campaign_header_title_txt()
    context.rewards_campaign_form_page.verify_header_warning_message()
    # context.rewards_campaign_form_page.verify_name_warning_message()
    context.rewards_campaign_form_page.verify_date_range_warning_message()
    context.rewards_campaign_form_page.verify_countries_warning_message()
    # context.rewards_campaign_form_page.verify_code_warning_message()
    context.rewards_campaign_form_page.verify_shipping_services_warning_message()
    context.rewards_campaign_form_page.verify_add_at_least_one_discount_or_commission_warning_message()
    context.execute_steps(u"""
                      then I can cancel the campaign""")


@when('fill in detail for an order-level campaign')
def step_impl(context):
    for row in context.table:
        context.rewards_campaign_form_page = Form(context)
        # context.rewards_campaign_form_page.click_campaign_type_drop_down()
        context.rewards_campaign_form_page.click_order_level_campaign_type_option()
        context.campaign_name_created = enter_campaign_detail(context, row)
        enter_order_level_campaign_discount_detail(context, row)
        enter_campaign_commission_detail(context, row)


@when('fill in detail for an item-level campaign')
def step_impl(context):
    for row in context.table:
        context.rewards_campaign_form_page = Form(context)
        context.rewards_campaign_form_page.click_item_level_campaign_type_option()
        context.campaign_name_created = enter_campaign_detail(context, row)
        context.rewards_campaign_form_page.select_products(row['product'])
        enter_item_level_campaign_discount_detail(context, row)
        enter_campaign_commission_detail(context, row)


@when('fill in detail for an many countries item-level campaign')
def step_impl(context):
    for row in context.table:
        context.rewards_campaign_form_page = Form(context)
        context.rewards_campaign_form_page.click_item_level_campaign_type_option()
        context.campaign_name_created = enter_campaign_detail_many_countries(context, row)
        context.rewards_campaign_form_page.select_products(row['product'])
        enter_item_level_campaign_discount_detail(context, row)
        enter_campaign_commission_detail(context, row)


@when('fill in detail for a rcode-order-level campaign')
def step_impl(context):
    for row in context.table:
        context.rewards_campaign_form_page = Form(context)
        # context.rewards_campaign_form_page.click_campaign_type_drop_down()
        context.rewards_campaign_form_page.click_rcode_order_level_campaign_type_option()
        context.campaign_name_created = enter_campaign_detail(context, row)
        enter_campaign_rcode(context, row)
        enter_order_level_campaign_discount_detail(context, row)
        enter_campaign_commission_detail(context, row)


@when('fill in detail for a rcode-item-level campaign')
def step_impl(context):
    for row in context.table:
        context.rewards_campaign_form_page = Form(context)
        # context.rewards_campaign_form_page.click_campaign_type_drop_down()
        context.rewards_campaign_form_page.click_rcode_item_level_campaign_type_option()
        context.campaign_name_created = enter_campaign_detail(context, row)
        enter_campaign_rcode(context, row)
        context.rewards_campaign_form_page.select_products(row['product'])
        enter_item_level_campaign_discount_detail(context, row)
        enter_campaign_commission_detail(context, row)


@when('fill in detail for a shipping-credit campaign')
def step_impl(context):
    context.browser.get_webdriver().refresh()
    time.sleep(5)
    for row in context.table:
        context.rewards_campaign_form_page = Form(context)
        context.rewards_campaign_form_page.click_shipping_credit_campaign_type_option()
        enter_shipping_credit_campaign_details(context)
        enter_campaign_shipping_credit_detail(context, row)


@when('fill in detail for a rcode_shipping-credit campaign')
def step_impl(context):
    for row in context.table:
        context.rewards_campaign_form_page = Form(context)
        # context.rewards_campaign_form_page.click_campaign_type_drop_down()
        context.rewards_campaign_form_page.click_rcode_shipping_credit_campaign_type_option()
        enter_shipping_credit_campaign_details(context)
        enter_campaign_rcode(context, row)
        enter_campaign_shipping_credit_detail(context, row)


def enter_updated_campaign_name(context):
    context.rewards_campaign_form_page = Form(context)
    context.updated_campaign_name = context.rewards_campaign_form_page.enter_updated_campaign_name()
    return context.updated_campaign_name


def enter_campaign_detail(context, row):
    context.rewards_campaign_form_page = Form(context)
    context.campaign_name = context.rewards_campaign_form_page.enter_campaign_name()
    context.rewards_campaign_form_page.click_start_date_calendar()
    context.rewards_campaign_form_page.select_today_date_from_calendar()
    context.rewards_campaign_form_page.click_start_hour_drop_down()
    context.rewards_campaign_form_page.select_start_hour_option()
    context.rewards_campaign_form_page.click_end_hour_drop_down()
    context.rewards_campaign_form_page.select_end_hour_option()
    context.rewards_campaign_form_page.select_platform(row['platform'])
    context.rewards_campaign_form_page.exclude_country()
    context.rewards_campaign_form_page.click_end_date_calendar()
    context.rewards_campaign_form_page.select_today_date_from_calendar()
    return context.campaign_name


def enter_campaign_detail_many_countries(context, row):
    context.rewards_campaign_form_page = Form(context)
    context.campaign_name = context.rewards_campaign_form_page.enter_campaign_name()
    context.rewards_campaign_form_page.click_start_date_calendar()
    context.rewards_campaign_form_page.select_today_date_from_calendar()
    context.rewards_campaign_form_page.click_start_hour_drop_down()
    context.rewards_campaign_form_page.select_start_hour_option()
    context.rewards_campaign_form_page.click_end_hour_drop_down()
    context.rewards_campaign_form_page.select_end_hour_option()
    context.rewards_campaign_form_page.select_platform(row['platform'])
    context.rewards_campaign_form_page.many_country()
    context.rewards_campaign_form_page.click_end_date_calendar()
    context.rewards_campaign_form_page.select_today_date_from_calendar()
    return context.campaign_name


def enter_campaign_rcode(context, row):
    context.rewards_campaign_form_page.select_code(row['referral_code'])
    context.rewards_campaign_form_page.click_code_add_btn()


def enter_order_level_campaign_discount_detail(context, row):
    context.rewards_campaign_form_page.enter_new_customers_discount_value(row['dis_new_cus_val'])
    context.rewards_campaign_form_page.enter_new_customers_min_order_value(row['dis_new_cus_min_order_val'])
    context.rewards_campaign_form_page.enter_existing_customers_discount_value(row['dis_exis_cus_val'])
    context.rewards_campaign_form_page.enter_existing_customers_min_order_value(row['dis_exis_cus_min_order_val'])
    context.rewards_campaign_form_page.enter_limit_for_discount(row['dis_limit_num'])


def enter_item_level_campaign_discount_detail(context, row):
    context.rewards_campaign_form_page.enter_new_customers_discount_value(row['dis_new_cus_val'])
    context.rewards_campaign_form_page.enter_existing_customers_discount_value(row['dis_exis_cus_val'])
    context.rewards_campaign_form_page.enter_limit_for_discount(row['dis_limit_num'])


def enter_campaign_commission_detail(context, row):
    context.rewards_campaign_form_page.enter_new_customers_commission_value(row['commission_new_cus_val'])
    context.rewards_campaign_form_page.enter_existing_customers_commission_value(row['commission_exis_cus_val'])
    context.rewards_campaign_form_page.enter_limit_for_commission(row['commission_limit_num'])


def enter_shipping_credit_campaign_details(context):
    context.rewards_campaign_form_page = Form(context)
    context.campaign_name = context.rewards_campaign_form_page.enter_campaign_name()
    context.logger.info('Campaign name: ' + context.campaign_name)
    context.rewards_campaign_form_page.click_start_date_calendar()
    context.rewards_campaign_form_page.select_today_date_from_calendar()
    context.rewards_campaign_form_page.click_start_hour_drop_down()
    context.rewards_campaign_form_page.select_start_hour_option()
    context.rewards_campaign_form_page.click_end_hour_drop_down()
    context.rewards_campaign_form_page.select_end_hour_option()
    context.rewards_campaign_form_page.click_end_date_calendar()
    context.rewards_campaign_form_page.select_today_date_from_calendar()
    context.rewards_campaign_form_page.click_all_countries_radio_btn()
    context.rewards_campaign_form_page.click_all_shipping_services_radio_btn()


def enter_campaign_shipping_credit_detail(context, row):
    context.rewards_campaign_form_page.enter_new_customers_shipping_credit_value(row['new_cus_shipping_credit_val'])
    context.rewards_campaign_form_page.enter_new_customers_min_order_value(row['shipping_new_cus_min_order_val'])
    context.rewards_campaign_form_page.enter_existing_customers_shipping_credit_value(
        row['existing_cus_shipping_credit_val'])
    context.rewards_campaign_form_page.enter_existing_customers_min_order_value(row['shipping_exis_cus_min_order_val'])


@then('I can cancel the campaign')
def step_impl(context):
    context.rewards_campaign_form_page.click_cancel_btn()
    context.rewards_campaign_form_page.click_modal_confirm_btn()


@then('I can create a campaign')
def step_impl(context):
    context.rewards_campaign_form_page.save_new_campaign()
    # context.rewards_campaign_form_page.click_modal_confirm_btn()


@then('I can update order-level campaigns')
def step_impl(context):
    context.campaign_name = context.rewards_campaign_form_page.enter_campaign_name()
    for row in context.table:
        enter_order_level_campaign_discount_detail(context, row)
        enter_campaign_commission_detail(context, row)
        context.rewards_campaign_form_page.save_new_campaign()
        # context.rewards_campaign_form_page.click_modal_confirm_btn()
        context.rewards_campaign_list_page.click_clear_btn()


@then('I can update item-level campaigns')
def step_impl(context):
    context.campaign_name = context.rewards_campaign_form_page.enter_campaign_name()
    for row in context.table:
        enter_item_level_campaign_discount_detail(context, row)
        enter_campaign_commission_detail(context, row)
        context.rewards_campaign_form_page.save_and_confirm_campaign()
        # context.rewards_campaign_form_page.click_modal_confirm_btn()
        context.rewards_campaign_list_page.click_clear_btn()


@then('I can update shipping-credit campaigns')
def step_impl(context):
    context.browser.get_webdriver().refresh()
    time.sleep(15)
    context.campaign_name = context.rewards_campaign_form_page.enter_campaign_name()
    logger.info("Changed campaign name to " + context.campaign_name)
    for row in context.table:
        enter_campaign_shipping_credit_detail(context, row)
        context.rewards_campaign_form_page.save_and_confirm_campaign()
        # context.rewards_campaign_form_page.click_modal_confirm_btn()
        context.rewards_campaign_list_page.click_clear_btn()


@then('I can approve a campaign')
def step_impl(context):
    context.rewards_campaign_list_page.click_first_campaign_in_list_view(context.campaign_name)
    context.rewards_campaign_form_page.click_approve_btn()
    context.rewards_campaign_form_page.click_modal_confirm_btn()


@then('I can deactivate a campaign')
def step_impl(context):
    context.browser.get_webdriver().refresh()
    time.sleep(5)
    context.rewards_campaign_form_page.click_deactivate_btn()
    context.rewards_campaign_form_page.click_modal_confirm_btn()


@then('click list view campaigns tab')
def step_impl(context):
    context.rewards_campaign_list_page.click_list_view_campaigns_tab()


@then('click list view r_code tab')
def step_impl(context):
    context.rewards_campaign_list_page.click_list_view_r_code_tab()


@then('click list view shipping-credit tab')
def step_impl(context):
    context.rewards_campaign_list_page.click_list_view_shipping_credit_tab()


@then('click list view archived tab')
def step_impl(context):
    context.rewards_campaign_list_page.click_list_view_archived_tab()


@then('campaign created successfully')
def step_impl(context):
    context.rewards_campaign_list_page = List(context)
    context.rewards_campaign_list_page.search_country_or_campaign_name_or_rcode()
    # context.rewards_campaign_list_page.click_list_view_start_date_calendar()
    # context.rewards_campaign_form_page.select_today_date_from_calendar()
    # context.rewards_campaign_list_page.click_list_view_end_date_calendar()
    # context.rewards_campaign_form_page.select_today_date_from_calendar()
    # context.rewards_campaign_list_page.click_search_btn()
    context.rewards_campaign_list_page.search_and_verify_first_campaign_in_list_view(context.campaign_name)


# @then ('created rcode-item-campaign successfully')
# def step_impl(context):
#     # context.rewards_campaign_form_page = Form(context)
#     context.rewards_campaign_list_page = List(context)
#     # context.rewards_campaign_form_page.click_phoebe_campaign_type_drop_down()
#     # context.rewards_campaign_form_page.click_phoebe_item_campaign_type_option()
#     # context.rewards_campaign_form_page.click_phoebe_search_button()
#     context.rewards_campaign_list_page.search_and_verify_first_campaign_in_list_view(context.campaign_name)
#
#
# @then('created rcode-order-campaign successfully')
# def step_impl(context):
#     # context.rewards_campaign_form_page = Form(context)
#     context.rewards_campaign_list_page = List(context)
#     # context.rewards_campaign_form_page.click_phoebe_campaign_type_drop_down()
#     # context.rewards_campaign_form_page.click_phoebe_order_campaign_type_option()
#     # context.rewards_campaign_form_page.click_phoebe_search_button()
#     context.rewards_campaign_list_page.search_and_verify_first_campaign_in_list_view(context.campaign_name)
#
#
# @then ('created item-campaign successfully')
# def step_impl(context):
#     context.rewards_campaign_form_page = Form(context)
#     context.rewards_campaign_list_page = List(context)
#     # context.rewards_campaign_form_page.click_phoebe_campaign_type_drop_down()
#     # context.rewards_campaign_form_page.click_phoebe_item_campaign_type_option()
#     # context.rewards_campaign_form_page.click_phoebe_search_button()
#     context.rewards_campaign_list_page.search_and_verify_first_campaign_in_list_view(context.campaign_name)

@then('created {type} successfully')
def step_impl(context, type):
    context.rewards_campaign_form_page = Form(context)
    context.rewards_campaign_list_page = List(context)
    # context.rewards_campaign_form_page.click_phoebe_campaign_type_drop_down()
    # context.rewards_campaign_form_page.click_phoebe_order_campaign_type_option()
    # context.rewards_campaign_form_page.click_phoebe_search_button()
    context.rewards_campaign_list_page.search_and_verify_first_campaign_in_list_view(context.campaign_name, type)


@then('campaign updated successfully')
def step_impl(context):
    context.rewards_campaign_list_page.search_country_or_campaign_name_or_rcode()
    # context.rewards_campaign_list_page.click_list_view_start_date_calendar()
    # context.rewards_campaign_form_page.select_today_date_from_calendar()
    # context.rewards_campaign_list_page.click_list_view_end_date_calendar()
    # context.rewards_campaign_form_page.select_today_date_from_calendar()
    # context.rewards_campaign_list_page.click_search_btn()
    context.rewards_campaign_list_page.search_and_verify_first_campaign_in_list_view(context.campaign_name)


@then('campaign deactivated successfully')
def step_impl(context):
    context.rewards_campaign_list_page = List(context)
    context.rewards_campaign_list_page.search_country_or_campaign_name_or_rcode()
    context.rewards_campaign_list_page.click_list_view_start_date_calendar()
    context.rewards_campaign_form_page.select_today_date_from_calendar()
    context.rewards_campaign_list_page.click_list_view_end_date_calendar()
    context.rewards_campaign_form_page.select_today_date_from_calendar()
    # context.rewards_campaign_list_page.click_search_btn()
    context.rewards_campaign_list_page.search_and_verify_first_campaign_in_list_view(context.campaign_name)
    context.rewards_campaign_list_page.click_first_campaign_in_list_view(context.campaign_name)
    context.rewards_campaign_form_page.verify_deactivated_txt()
    context.rewards_campaign_form_page.click_cancel_btn()


@then('search first item level campaign')
def step_impl(context):
    context.rewards_campaign_list_page = List(context)
    context.rewards_campaign_list_page.search_country_or_campaign_name_or_rcode()
    time.sleep(8)


@then('search created campaign')
def step_impl(context):
    context.rewards_campaign_list_page = List(context)
    context.rewards_campaign_list_page.search_country_or_campaign_name_or_rcode()
    time.sleep(8)
    context.rewards_campaign_list_page.wait_search_page_load()
    # context.rewards_campaign_list_page.click_list_view_start_date_calendar()
    # context.rewards_campaign_form_page.select_today_date_from_calendar()
    # context.rewards_campaign_list_page.click_list_view_end_date_calendar()
    # context.rewards_campaign_form_page.select_today_date_from_calendar()
    # context.rewards_campaign_list_page.click_search_btn()
    context.rewards_campaign_list_page.search_and_verify_first_campaign_in_list_view(context.campaign_name)
    # context.rewards_campaign_list_page.search_and_verify_first_campaign_in_list_view()
    # context.rewards_campaign_list_page.click_first_campaign_in_list_view()
    context.rewards_campaign_list_page.click_first_campaign_in_list_view(context.campaign_name)
    create_new_rewards_campaign_page = Form(context)
    context.campaign_id = create_new_rewards_campaign_page.get_campaign_id()


@then('search created shipping credit campaign')
def step_impl(context):
    context.rewards_campaign_list_page.click_first_campaign_in_list_view(context.campaign_name)
    BehavePatcher(context, context.scenario).insert_png_to_allure_report("Check step")
    create_new_rewards_campaign_page = Form(context)
    BehavePatcher(context, context.scenario).insert_png_to_allure_report("Check step")
    context.campaign_id = create_new_rewards_campaign_page.get_campaign_id()
    BehavePatcher(context, context.scenario).insert_png_to_allure_report("Check step")


@then('campaign shipping-credit deactivated successfully')
def step_impl(context):
    context.rewards_campaign_list_page.click_first_campaign_in_list_view(context.campaign_name)
    context.rewards_campaign_form_page.verify_deactivated_txt()
    context.rewards_campaign_form_page.click_cancel_btn()


@then('select first campaign in list page')
def step_impl(context):
    context.rewards_campaigns_page.click_first_campaign_in_list_view(context.campaign_name)


@then('wait {number} seconds for data update')
def wait_for_data_update(context, number):
    time.sleep(int(number))


@then('I go to the rcode list')
def step_impl(context):
    context.rewards_campaign_form_page = Form(context)
    context.rewards_campaign_form_page.click_rcode_tab()


@then('click the correct reward I want')
def step_impl(context):
    context.rewards_campaign_form_page = Form(context)
    context.rewards_campaign_form_page.click_campaign_which_I_want(context.campaign_name_created)


#
# @when('click on save button without entering item-level rewards campaigns mandatory details')
# def step_impl(context):
#     context.rewards_campaign_form_page = Form(context)
#     context.rewards_campaign_form_page.click_item_level_chk_box()
#     context.rewards_campaign_form_page.click_save_btn()
#
#
# @then('I can see the item-level warning messages')
# def step_impl(context):
#     context.rewards_campaign_form_page.verify_create_new_campaign_header_title_txt()
#     context.rewards_campaign_form_page.verify_item_level_rewards_campaigns_header_warning_message()
#     context.rewards_campaign_form_page.verify_products_warning_message()
#     context.rewards_campaign_form_page.verify_add_at_least_one_discount_or_commission_warning_message()
#     context.rewards_campaign_form_page.verify_countries_warning_message()
#     context.execute_steps(u"""
#                       then I can cancel the rewards campaigns""")


# @when('enter the item-level rewards campaigns details')
# def step_impl(context):
#     for row in context.table:
#         enter_new_item_level_rewards_campaign_details(context, row)
#         enter_item_level_discount_details(context, row)
#         enter_commission_details(context, row)


# def enter_new_item_level_rewards_campaign_details(context, row):
#     context.rewards_campaign_form_page = Form(context)
#     context.rewards_campaign_form_page.click_campaign_type_drop_down()
#     context.rewards_campaign_form_page.click_standard_campaign_type_option()
#     context.rewards_campaign_form_page.enter_campaign_name()
#     context.rewards_campaign_form_page.click_start_date_calendar()
#     context.rewards_campaign_form_page.select_today_date_from_calendar()
#     context.rewards_campaign_form_page.click_start_hour_drop_down()
#     context.rewards_campaign_form_page.select_start_hour_option()
#     context.rewards_campaign_form_page.click_end_hour_drop_down()
#     context.rewards_campaign_form_page.select_end_hour_option()
#     context.rewards_campaign_form_page.click_end_date_calendar()
#     context.rewards_campaign_form_page.select_today_date_from_calendar()
#     # context.rewards_campaign_form_page.select_a_platform(row['platform'])
#     # context.rewards_campaign_form_page.select_country(row['country'])
#     context.rewards_campaign_form_page.click_all_countries_radio_btn()
#     # context.rewards_campaign_form_page.select_rewards_code(row['rewards_code'])
#     # context.rewards_campaign_form_page.click_rewards_code_add_btn()
#     context.rewards_campaign_form_page.click_all_rewards_code_radio_btn()
#     context.rewards_campaign_form_page.click_item_level_chk_box()
#     context.rewards_campaign_form_page.select_products(row['product'])


@given("jane test fail")
def jane_test_fail(context):
    assert 1 == 2, "jane test fail"


@given("janeteststep")
def janeteststep(context):
    print("janetest pass")

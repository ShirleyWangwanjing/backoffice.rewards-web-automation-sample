## Created by rsekaran at 11/12/2019
#@fixture.browser.rewards
#Feature: Create/Update/Deactivate a shipping-credit campaign
#
#  @smoke_test
#  Scenario: When the user click the submit button without entering the mandatory details in shipping-credit campaign validate the warning messages
#  Given test_user_editor can enter the username and password
#  Given I can go to the create page
#  When click on the submit button without entering mandatory details for a shipping-credit campaign
#  Then I can see the shipping-credit warning messages at header
#
#  @smoke_test
#  Scenario: As a user I can cancel a shipping-credit campaign
#    Given test_user_editor can enter the username and password
#    Given I can go to the create page
#    When fill in detail for a shipping-credit campaign
#    |new_cus_shipping_credit_val|existing_cus_shipping_credit_val|shipping_new_cus_min_order_val|shipping_exis_cus_min_order_val|
#    |1                          |1                               |1                             |1                              |
#    Then I can cancel the campaign
#
#  @smoke_test
#  Scenario: As a user I can create and update a shipping-credit campaign and then deactivate it
#    Given test_user_editor can enter the username and password
#    Given I can go to the create page
#    When fill in detail for a shipping-credit campaign
#    |new_cus_shipping_credit_val|existing_cus_shipping_credit_val|shipping_new_cus_min_order_val|shipping_exis_cus_min_order_val|
#    |1                          |1                               |1                             | 1                             |
#    Then I can create a campaign
#    Then click list view shipping-credit tab
#    Then search created shipping credit campaign
#    Then I can update shipping-credit campaigns
#    |new_cus_shipping_credit_val|existing_cus_shipping_credit_val|shipping_new_cus_min_order_val|shipping_exis_cus_min_order_val|
#    |2                          |2                               |2                             | 2                             |
#    Then click list view shipping-credit tab
#    Then search created shipping credit campaign
#    Then I can deactivate a campaign
#    Then click list view shipping-credit tab
#    Then campaign shipping-credit deactivated successfully
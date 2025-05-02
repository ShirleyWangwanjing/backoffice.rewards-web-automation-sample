## Created by rsekaran at 11/12/2019
#@fixture.browser.rewards
#Feature: Create/Update/Deactivate a rcode-shipping-credit campaign
#
#  @smoke_test
#  Scenario: When the user click the submit button without entering the mandatory details in rcode-shipping_credit campaign validate the warning messages
#  Given test_user_editor can enter the username and password
#  Given I can go to the create page
#  When click on the submit button without entering mandatory details for a rcode-shipping-credit campaign
#  Then I can see the rcode-shipping-credit warning messages at header
#
#  @smoke_test
#  Scenario: As a user I can cancel a rcode-shipping-credit campaign
#  Given test_user_editor can enter the username and password
#  Given I can go to the create page
#  When fill in detail for a rcode_shipping-credit campaign
#  |referral_code|new_cus_shipping_credit_val|existing_cus_shipping_credit_val|shipping_new_cus_min_order_val|shipping_exis_cus_min_order_val|
#  |AAA0014      |1                          |1                               |1                             |1                              |
#  Then I can cancel the campaign
#
#  @smoke_test
#  Scenario: As a user I can create and update an rcode-shipping-credit campaign and then deactivate it
#  Given test_user_editor can enter the username and password
#  Given I can go to the create page
#  When fill in detail for a rcode_shipping-credit campaign
#  |referral_code|new_cus_shipping_credit_val|existing_cus_shipping_credit_val|shipping_new_cus_min_order_val|shipping_exis_cus_min_order_val|
#  |AAA0014      |1                          |1                               |1                             |1                              |
#  Then I can create a campaign
#  Then click list view shipping-credit tab
#  Then campaign created successfully
#    Then click list view shipping-credit tab
#  Then search created campaign
#  Then I can update shipping-credit campaigns
#  |referral_code|new_cus_shipping_credit_val|existing_cus_shipping_credit_val|shipping_new_cus_min_order_val|shipping_exis_cus_min_order_val|
#  |AAA0014      |2                          |2                               |2                             |2                              |
#  Then click list view shipping-credit tab
#    Then campaign updated successfully
#  Then click list view shipping-credit tab
#  Then search created campaign
#  Then I can deactivate a campaign
#  Then click list view shipping-credit tab
#  Then campaign deactivated successfully
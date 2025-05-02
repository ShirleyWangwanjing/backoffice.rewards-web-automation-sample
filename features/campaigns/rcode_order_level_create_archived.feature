# Created by nogu at 17/10/2019
@fixture.browser.rewards @fixture.sql_database.rewards
Feature: Create/Deactivate a rcode-order-level campaign

#  @smoke_test
#  Scenario: When the user click the submit button without entering the mandatory details in r-code-order-level campaign validate the warning messages
#  Given I can go to the create page
#  When click on the submit button without entering mandatory details for a rcode-order-level campaign
#  Then I can see the rcode-order-level warning messages at header
#
#  @smoke_test
#  Scenario: As a user I can cancel a rcode-order-level campaign
#  Given I can go to the create page
#  When fill in detail for a rcode-order-level campaign
#  |platform     |referral_code|dis_new_cus_val|dis_new_cus_min_order_val|dis_exis_cus_val|dis_exis_cus_min_order_val|commission_new_cus_val|commission_exis_cus_val|dis_limit_num|commission_limit_num|
#  |android-china|NNN000       |1              |1                        |1               |1                         |1                     |1                      |1            |1                   |
#  Then I can cancel the campaign

  @smoke_test
  Scenario: As a user I can create and deactivate an rcode-order-level campaign
    Given I can go to the create page
    When fill in detail for a rcode-order-level campaign
    |platform     |referral_code |dis_new_cus_val|dis_new_cus_min_order_val|dis_exis_cus_val|dis_exis_cus_min_order_val|commission_new_cus_val|commission_exis_cus_val|dis_limit_num|commission_limit_num|
    |android-china|NNN000        |1              |1                        |1               |1                         |1                     |1                      |1            |1                   |
    Then I can create a campaign
    Then click list view r_code tab
    Then created rcode-order-campaign successfully
    Then I go to the rcode list
    Then click the correct reward I want
    Then I deactivate the created campaign in list
    Then Verify the first campaign in archived tab

#  Then search created campaign
#  Then I can update order-level campaigns
#  |platform    |referral_code |dis_new_cus_val|dis_new_cus_min_order_val|dis_exis_cus_val|dis_exis_cus_min_order_val|commission_new_cus_val|commission_exis_cus_val|
#  |iphone-china|NNN000        |2              |2                        |2               |2                         |2                     |2                      |
#  Then wait 35 seconds for data update
#  Then campaign updated successfully



# Created by lliu at 22/10/2019
@fixture.browser.rewards @fixture.sql_database.rewards
Feature: Create/Deactivate an order-level campaign

#  @smoke_test
#  Scenario: When the user click the submit button without entering the mandatory details in r-code-order-level campaign validate the warning messages
#  Given I can go to the create page
#  When click on the submit button without entering mandatory details for an order-level campaign
#  Then I can see the order-level warning messages at header

#  @smoke_test
#  Scenario: As a user I can cancel an order-level campaign
#  Given I can go to the create page
#  When fill in detail for an order-level campaign
#  |platform     |referral_code|dis_new_cus_val|dis_new_cus_min_order_val|dis_exis_cus_val|dis_exis_cus_min_order_val|commission_new_cus_val|commission_exis_cus_val|dis_limit_num|commission_limit_num|
#  |android-china|NNN000       |1              |1                        |1               |1                         |1                     |1                      |1            |1                   |
#  Then I can cancel the campaign

  @smoke_test
  Scenario: As a user I can create and deactivate an order-level campaign
#  Given test_user_editor can enter the username and password
    Given I can go to the create page
    When fill in detail for an order-level campaign
    |platform     |referral_code |dis_new_cus_val|dis_new_cus_min_order_val|dis_exis_cus_val|dis_exis_cus_min_order_val|commission_new_cus_val|commission_exis_cus_val|dis_limit_num|commission_limit_num|
    |android-china|NNN000        |1              |1                        |1               |1                         |1                     |1                      |1            |1                   |
    Then I can create a campaign
    Then created order-campaign successfully
    Then click the correct reward I want
    Then I deactivate the created campaign in list
    Then Verify the first campaign in archived tab




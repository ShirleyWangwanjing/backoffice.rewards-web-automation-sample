# Created by rsekaran at 11/12/2019
@fixture.browser.rewards @fixture.sql_database.rewards
Feature: Cancel an item-level campaign

  @smoke_test
  Scenario: As a user I can cancel an item-level campaign
    Given I can go to the create page
    When fill in detail for an item-level campaign
    |platform     |referral_code|dis_new_cus_val|dis_new_cus_min_order_val|dis_exis_cus_val|dis_exis_cus_min_order_val|commission_new_cus_val|commission_exis_cus_val|product|dis_limit_num|commission_limit_num|
    |android-china|NNN000       |1              |1                        |1               |1                         |1                     |1                      |nat    |1            |1                   |
    Then I can cancel the campaign

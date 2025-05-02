# Created by rsekaran at 11/12/2019
@fixture.browser.rewards @fixture.sql_database.rewards
Feature: An item-level campaign warning message case

  @smoke_test
  Scenario: When the user click the submit button without entering the mandatory details in item-level campaign validate the warning messages
    Given I can go to the create page
    When click on the submit button without entering mandatory details for an item-level campaign
    Then I can see the rcode-item-level warning messages at header

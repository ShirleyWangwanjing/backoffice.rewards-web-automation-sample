# Created by ragu.sekaran at 25/06/2019

#@fixture.browser.rewards
#Feature: Validate the user roles and permission sets
#
#  @test
#  Scenario: As a reader role user I have the reader permissions
#  Then I have only reader role permissions
#
#  @test
#  Scenario: As a editor role user I have the related permissions
#  Then I have only editor role permissions
#
#  @test
#  Scenario: As a editor user I can create an item-level rewards campaigns
#  Given I can open a create rewards campaign window
#  When enter the item-level rewards campaigns details
#  |country |rewards_code|product |dis_new_cus_val|dis_exis_cus_val|commission_new_cus_val|commission_exis_cus_val|
#  |States  |MMM000      |cal     |1              |1               |1                     |1                      |
#  Then I can create rewards campaigns campaign
#  Then new rewards item-level campaigns created successfully
#  Then I can update item-level rewards campaigns
#  |country |rewards_code|dis_new_cus_val|dis_exis_cus_val|commission_new_cus_val|commission_exis_cus_val|
#  |States  |MMM010      |2              |2               |2                     |2                      |
#  Then new rewards item-level campaigns created successfully

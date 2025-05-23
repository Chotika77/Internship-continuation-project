# Created by dchku at 3/10/2025
Feature: Tests for the main page

  Scenario: User can filter by Presale
    Given open the main page
    When Log in to the page
    And change the filter to presale
    Then Verify each product contains Presale(EOI)


  Scenario: User can go to settings and see the right number of UI elements
    Given open the main page
    When Log in to the page
    And Click on settings option
    Then Verify the right page opens
    Then Verify there are 13 options for the settings
    Then Verify “Connect the company” button is available


  Scenario: User can filter by Out of Stock
    Given open the main page
    When Log in to the page
    And change the filter to Out of Stock
    Then Verify each product contains Out of stock


  Scenario: User can filter the Secondary deals by “want to buy” option
    Given open the main page
    When Log in to the page
    And Click on “Secondary” option at the left side menu
    Then Verify the right page opens
    When Click on Filters
    And Filter the products by “want to buy”
    And Click on Apply Filter
    Then Verify all cards have “Want to buy” tag

  Scenario: User can filter the Secondary deals by Unit price range
    Given open the main page
    When Log in to the page
    And Click on “Secondary” option at the left side menu
    Then Verify the right page opens
    When Click on Filters
    When Filter the products by price range from 1200000 to 2000000 AED
    Then Verify the price in all cards is inside the range 1200000 - 2000000

  Scenario: User can open the off plan page and go through the pagination
    Given open the main page
    When Log in to the page
    And Click on off plan option at the left side menu
    Then Verify the right page opens
    When Go to the final page using the pagination button
    And Go back to the first page using the pagination button

  Scenario: User can open market tab and filter by developers option
    Given open the main page
    When Log in to the page
    When Click on “market” at the left side menu
    Then Verify the right page opens
    When Click on Developers filter at the top of the page
    Then Verify all cards has the license tag

  Scenario:  User can click on verifications settings option and verify the right page opens
    Given open the main page
    When Log in to the page
    When Click on “settings” at the left side menu
    When Click on the verification option
    Then Verify the right page opens
    And  Verify “upload image” and “Next step” buttons are available





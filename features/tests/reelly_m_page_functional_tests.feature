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
# Created by dchku at 3/10/2025
Feature: Tests for the main page

  Scenario: User can filter by Presale
    Given open the main page
    When Log in to the page
    And change the filter to presale
    Then Verify each product contains the Presale
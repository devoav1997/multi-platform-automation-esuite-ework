Feature: Verify Company Detail after Creation

  Scenario: Confirm that the inputted company data is displayed correctly
    Given user is logged in to esuite
    When user creates a new company with dummy data
    Then user should see the new company listed on Companies page
    And user can view company details and see all inputted data correctly

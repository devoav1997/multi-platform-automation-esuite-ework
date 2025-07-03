Feature: Login to ework app

  Scenario: User logs in successfully
    Given the app is launched
    When user inputs login data
    And user taps on sign in
    Then user should see dashboard screen

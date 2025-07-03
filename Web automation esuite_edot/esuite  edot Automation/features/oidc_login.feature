Feature: OIDC Login Flow

  Scenario: Positive login with valid credentials
    Given user open OIDC login page
    When user clicks "Use Email or Username"
    And user input username "it.qa@edot.id"
    And user clicks "Log In"
    And user input password "it.QA2025"
    And user clicks "Log In"
    Then user should see dashboard page

  Scenario: Negative login with wrong password
    Given user open OIDC login page
    When user clicks "Use Email or Username"
    And user input username "it.qa@edot.id"
    And user clicks "Log In"
    And user input password "wrong_password"
    And user clicks "Log In"
    Then user should see incorrect password message

  Scenario: Negative login with wrong email format
    Given user open OIDC login page
    When user clicks "Use Email or Username"
    And user input username ": it.qa@edot.id"
    Then user should see "Wrong email format" message

  Scenario: Negative login with unregistered email
    Given user open OIDC login page
    When user clicks "Use Email or Username"
    And user input username "iTest@gmail.com"
    And user clicks "Log In"
    Then user should see "Email Not Registered" popup

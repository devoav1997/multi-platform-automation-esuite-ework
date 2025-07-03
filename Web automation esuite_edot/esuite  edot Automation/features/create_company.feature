Feature: Create New Company on esuite.edot.id

  Scenario: User successfully creates a new company using dummy data
    Given user is logged in to esuite
    When user navigates to Companies page
    And user clicks Add Company
    And user fills company registration form with dummy data
    And user goes to next company form and fill required fields
    And user completes branch creation form with dummy data
    Then user should see new company on Companies page

    

Feature: Create new customer

  Scenario: User creates a new customer
    Given user is logged in
    When user creates a customer with name "John Doe" and phone "08123456789"
    Then new customer "John Doe" should be displayed in customer list

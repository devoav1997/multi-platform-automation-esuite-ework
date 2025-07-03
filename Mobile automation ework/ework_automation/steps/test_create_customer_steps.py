from pytest_bdd import scenarios, given, when, then
from pages.login_page import LoginPage
from pages.customer_page import CustomerPage

scenarios('../features/create_customer.feature')

@given('user is logged in')
def user_logged_in(appium_driver):
    page = LoginPage(appium_driver)
    page.enter_company_id("5102777")
    page.enter_username("it.qa@edot.id")
    page.enter_password("it.QA2025")
    page.tap_sign_in()
    assert page.is_dashboard_displayed()

@when('user creates a customer with name "John Doe" and phone "08123456789"')
def create_customer(appium_driver):
    page = CustomerPage(appium_driver)
    page.create_customer("John Doe", "08123456789")

@then('new customer "John Doe" should be displayed in customer list')
def check_customer(appium_driver):
    page = CustomerPage(appium_driver)
    assert page.is_customer_in_list("John Doe")

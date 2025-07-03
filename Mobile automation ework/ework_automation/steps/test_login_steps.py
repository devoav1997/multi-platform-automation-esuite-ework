from pytest_bdd import scenarios, given, when, then
from pages.login_page import LoginPage

scenarios('../features/login.feature')

@given('the app is launched')
def app_launched(appium_driver):
    pass  # Driver sudah launch via fixture

@when('user inputs login data')
def input_login(appium_driver):
    page = LoginPage(appium_driver)
    page.enter_company_id("5102757")
    page.enter_username("it.qa@edot.id")
    page.enter_password("it.QA2025")

@when('user taps on sign in')
def tap_login(appium_driver):
    page = LoginPage(appium_driver)
    page.tap_sign_in()

@then('user should see dashboard screen')
def dashboard_appears(appium_driver):
    page = LoginPage(appium_driver)
    assert page.is_dashboard_displayed()

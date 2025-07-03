from behave import given, when, then
from selenium import webdriver
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time
from selenium.webdriver.chrome.service import Service

@given('user open OIDC login page')
def step_open_oidc(context):
    options = webdriver.ChromeOptions()
    # options.add_argument("--headless")  
    context.driver = webdriver.Chrome(
        service=Service(ChromeDriverManager().install()),
        options=options
    )
    context.driver.get("https://esuite.edot.id")
    context.driver.implicitly_wait(5)

@when('user clicks "Use Email or Username"')
def step_click_email_username(context):
    btn = WebDriverWait(context.driver, 10).until(
        EC.element_to_be_clickable((By.XPATH, "//button[contains(., 'Use Email or Username')]"))
    )
    btn.click()
    time.sleep(1)

@when('user input username "{username}"')
def step_input_username(context, username):
    username_input = WebDriverWait(context.driver, 10).until(
        EC.visibility_of_element_located((By.XPATH, "//input[@placeholder='Input Email or Username']"))
    )
    username_input.clear()
    username_input.send_keys(username)
    time.sleep(1)

@when('user clicks "Log In"')
def step_click_login(context):
    login_btn = WebDriverWait(context.driver, 10).until(
        EC.element_to_be_clickable((By.XPATH, "//button[contains(., 'Log In')]"))
    )
    login_btn.click()
    time.sleep(2)

@when('user input password "{password}"')
def step_input_password(context, password):
    password_input = WebDriverWait(context.driver, 10).until(
        EC.visibility_of_element_located((By.XPATH, "//input[@placeholder='Password']"))
    )
    password_input.clear()
    password_input.send_keys(password)
    time.sleep(1)

@then('user should see dashboard page')
def step_dashboard(context):
    dashboard_greeting = WebDriverWait(context.driver, 10).until(
        EC.presence_of_element_located((By.XPATH, "//*[contains(text(), 'Welcome Back')]"))
    )
    assert dashboard_greeting.is_displayed()
    context.driver.quit()

@then('user should see incorrect password message')
def step_incorrect_password(context):
    error_msg = WebDriverWait(context.driver, 10).until(
        EC.visibility_of_element_located((By.XPATH, "//p[text()='Incorrect password']"))
    )
    assert error_msg.is_displayed()
    context.driver.quit()

@then('user should see "Wrong email format" message')
def step_wrong_email_format(context):
    error_msg = WebDriverWait(context.driver, 5).until(
        EC.visibility_of_element_located((By.XPATH, "//p[text()='Wrong email format']"))
    )
    assert error_msg.is_displayed()
    context.driver.quit()

@then('user should see "Email Not Registered" popup')
def step_email_not_registered(context):
    popup_title = WebDriverWait(context.driver, 10).until(
        EC.visibility_of_element_located((By.XPATH, "//*[contains(text(), 'Email Not Registered')]"))
    )
    assert popup_title.is_displayed()
    context.driver.quit()

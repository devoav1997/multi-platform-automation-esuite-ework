from appium.webdriver.common.appiumby import AppiumBy
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

class LoginPage:
    def __init__(self, driver):
        self.driver = driver

    def enter_company_id(self, company_id):
        field = self.driver.find_element(AppiumBy.ID, "id.edot.ework.debug:id/tv_company_id")
        field.clear()
        field.send_keys(company_id)

    def enter_username(self, username):
        field = self.driver.find_element(AppiumBy.ID, "id.edot.ework.debug:id/tv_username")
        field.clear()
        field.send_keys(username)

    def enter_password(self, password):
        field = self.driver.find_element(AppiumBy.ID, "id.edot.ework.debug:id/tv_password")
        field.clear()
        field.send_keys(password)

    def tap_sign_in(self):
        btn = self.driver.find_element(AppiumBy.ID, "id.edot.ework.debug:id/btn_signin")
        btn.click()

    def is_dashboard_displayed(self):
        try:
            WebDriverWait(self.driver, 10).until(
                EC.presence_of_element_located((
                    AppiumBy.XPATH, '//*[contains(@text, "Dashboard") or contains(@text, "dashboard") or contains(@text, "Beranda")]'
                ))
            )
            return True
        except:
            return False

from appium.webdriver.common.appiumby import AppiumBy
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

class CustomerPage:
    def __init__(self, driver):
        self.driver = driver

    def create_customer(self, name, phone):
  
        self.driver.find_element(AppiumBy.ACCESSIBILITY_ID, "add_customer_button").click()
        self.driver.find_element(AppiumBy.XPATH, '//android.widget.EditText[contains(@text, "Name")]').send_keys(name)
        self.driver.find_element(AppiumBy.XPATH, '//android.widget.EditText[contains(@text, "Phone")]').send_keys(phone)
        self.driver.find_element(AppiumBy.ACCESSIBILITY_ID, "save_button").click()

    def is_customer_in_list(self, name):
        try:
            WebDriverWait(self.driver, 10).until(
                EC.presence_of_element_located(
                    (AppiumBy.XPATH, f'//android.widget.TextView[@text="{name}"]')
                )
            )
            return True
        except:
            return False

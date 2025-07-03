import pytest
from appium import webdriver
from appium.options.android import UiAutomator2Options

@pytest.fixture(scope="session")
def appium_driver():
    options = UiAutomator2Options()
    options.platform_name = "Android"
    options.automation_name = "UiAutomator2"
    options.device_name = "emulator-5554"  # Ganti sesuai nama device-mu!
    options.app = "/Users/devo/Downloads/ework 1.20.5.apk"
    options.app_package = "id.edot.ework.debug"
    options.app_activity = "id.edot.onboarding.ui.splash.SplashScreenActivity"
    options.auto_grant_permissions = True


    driver = webdriver.Remote("http://localhost:4723", options=options)
    yield driver
    driver.quit()

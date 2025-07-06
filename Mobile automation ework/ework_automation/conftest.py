import os
import pytest
from appium import webdriver
from appium.options.android import UiAutomator2Options

@pytest.fixture(scope="session")
def appium_driver():
    # Ambil direktori base project (tempat conftest.py berada)
    base_dir = os.path.dirname(os.path.abspath(__file__))
    # Path relatif ke APK (dari posisi conftest.py)
    apk_path = os.path.join(base_dir, "ework 1.20.5.apk")
    
    options = UiAutomator2Options()
    options.platform_name = "Android"
    options.automation_name = "UiAutomator2"
    options.device_name = "emulator-5554"
    options.app = apk_path
    options.app_package = "id.edot.ework.debug"
    options.app_activity = "id.edot.onboarding.ui.splash.SplashScreenActivity"
    options.auto_grant_permissions = True

    driver = webdriver.Remote("http://localhost:4723", options=options)
    yield driver
    driver.quit()

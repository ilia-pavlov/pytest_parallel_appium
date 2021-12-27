from appium import webdriver
from pages.access_code_input import Access_code
import pytest

@pytest.mark.parametrize('udid, deviceName, systemPort',
                         [('4639444a50393498', 's9', '8201'),
                          ('emulator-5554', 'Pixel_3a_API_28', '8202'),
                          ('emulator-5556', 'Samsung_G_A71', '8203'),
                          ('emulator-5558', 'Nexus', '8204')] )
def  test_access_code_input(udid, deviceName, systemPort):
    desired_cap = {
        "platformName": "Android",
        "platformVersion": "10",
        "deviceName": deviceName,
        "app": "os.path.XXXXXXXX",      """app location """
        "appPackage": "com.clicktherapeuticsdev.alpha.ct101",
        "autoAcceptAlerts": "true",
        "automationName": "UiAutomator2",
        "udid": udid,
        "systemPort": int(systemPort)
    }

    APPIUM_HUB = 'http://127.0.0.1:4723/wd/hub'
    driver = webdriver.Remote(APPIUM_HUB, desired_cap)
    driver.implicitly_wait(10)

    access_code_input = Access_code(driver)
    access_code_input.access_code_input()

# device S9
# Pixel_3a_API_28
# Samsung_G_A71_5.4
# Galaxy_Nexus_API_27_4.65
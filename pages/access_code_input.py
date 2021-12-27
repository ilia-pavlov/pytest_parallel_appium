
import time


class Access_code():
    def __init__(self, driver):
        self.driver = driver

    def access_code_input(self):
        GET_STARTED_BUTTON = "marketing-animation-sign-up-button"
        self.driver.find_element_by_accessibility_id(GET_STARTED_BUTTON).click()

        ACCESS_CODE_FILED = "sign-up-code-input"
        ACCESS_CODE = 'XXXXXXXX'

        input_filed = self.driver.find_element_by_accessibility_id(ACCESS_CODE_FILED)
        time.sleep(1)
        input_filed.clear()
        input_filed.send_keys(ACCESS_CODE)





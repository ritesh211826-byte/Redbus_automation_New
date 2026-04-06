from selenium.webdriver.common.by import By
from utils.wait_utils import WaitUtils
import time

class PassengerPage:

    def __init__(self, driver):
        self.driver = driver
        self.wait = WaitUtils(driver)

    PASSENGER_SECTION = (By.XPATH, "//span[normalize-space()='3. Passenger Info']")

    EMAIL = (By.XPATH, "//input[@id='0_5']")
    PHONE = (By.XPATH, "//input[@id='0_6']")
    NAME = (By.XPATH, "//input[@id='0_4']")
    AGE = (By.XPATH, "//input[@id='0_1']")
    MALE = (By.XPATH, "//div[contains(@aria-label,'Male')]")
    CONTINUE = (By.XPATH, "//button[contains(text(),'Continue')]")

    # 🔥 ADD THIS METHOD
    def open_passenger_section(self):
        self.wait.click(self.PASSENGER_SECTION)
        print("✅ Passenger section opened")

    def fill_details(self):
        self.wait.send_keys(self.EMAIL, "test@gmail.com")
        self.wait.send_keys(self.PHONE, "9999999999")
        self.wait.send_keys(self.NAME, "Ritesh")
        self.wait.send_keys(self.AGE, "26")
        # 🔥 Wait for animation
        time.sleep(1)

        # 🔥 Click male with retry
        try:
            self.wait.click(self.MALE)
            print("✅ Male selected (normal click)")
        except:
            self.driver.execute_script(
                "arguments[0].click();",
                self.driver.find_element(*self.MALE)
            )
            print("✅ Male selected (JS click)")

    def click_continue(self):
        self.wait.click(self.CONTINUE)
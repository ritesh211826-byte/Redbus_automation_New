from selenium.webdriver.common.by import By
from utils.wait_utils import WaitUtils
from selenium.webdriver.support import expected_conditions as EC
import time

class PassengerPage:

    def __init__(self, driver):
        self.driver = driver
        self.wait = WaitUtils(driver)

    PASSENGER_SECTION = (By.XPATH, "//div[@aria-label='Passenger Info']")

    EMAIL = (By.XPATH, "//input[@id='0_5']")
    PHONE = (By.XPATH, "//input[@id='0_6']")
    NAME = (By.XPATH, "//input[@id='0_4']")
    AGE = (By.XPATH, "//input[@id='0_1']")
    MALE = (
        By.XPATH,
        "//div[contains(@class,'passengerInfoWrap')]//span[text()='Male']"
    )
    CONTINUE = (By.XPATH, "//button[contains(text(),'Continue')]")

    # 🔥 ADD THIS METHOD
    # def open_passenger_section(self):
    #     print("Waiting for passenger section...")
    #     self.wait.click(self.PASSENGER_SECTION)
    def open_passenger_section(self):
        print("Opening passenger section...")

        element = self.wait.wait.until(
            EC.presence_of_element_located(self.PASSENGER_SECTION)
        )

        # scroll into view
        self.driver.execute_script("arguments[0].scrollIntoView();", element)

        # click using JS
        self.driver.execute_script("arguments[0].click();", element)

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
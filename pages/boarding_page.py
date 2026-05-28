from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time

class BoardingPage:

    def __init__(self, driver):
        self.driver = driver

    BOARDING_SECTION = (By.XPATH, "//div[contains(@aria-label,'Board/Drop point')]")
    BOARDING_POINT = (By.XPATH, "//div[contains(@id,'bp-point')][1]")
    DROPPING_POINT = (By.XPATH, "//div[@aria-label='Dropping points']//label[@for='bp-point-0']")

    def select_boarding_and_dropping(self):

        wait = WebDriverWait(self.driver, 20)

        # Open boarding section
        wait.until(EC.element_to_be_clickable(self.BOARDING_SECTION)).click()
        print("✅ Boarding section opened")


        boarding = wait.until(EC.element_to_be_clickable(self.BOARDING_POINT))
        self.driver.execute_script("arguments[0].click();", boarding)
        print("✅ Boarding point selected")

        # 🔥 wait for DOM refresh
       #wait.until(EC.staleness_of(boarding))

        print(" ✅ Waiting for dropping points...")

        # Select dropping point
        droppings = wait.until(EC.presence_of_all_elements_located(self.DROPPING_POINT))
        self.driver.execute_script("arguments[0].click();", droppings[0])

        print("✅ Dropping point selected")
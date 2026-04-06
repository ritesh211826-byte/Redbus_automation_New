from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

class BoardingPage:

    def __init__(self, driver):
        self.driver = driver

    BOARDING_SECTION = (By.XPATH, "//div[contains(@aria-label,'Board/Drop point')]")
    BOARDING_POINT = (By.XPATH, "//div[contains(@id,'bp-point')][1]")
    DROPPING_POINT = (By.XPATH, "(//div[@aria-label='Dropping points']//div[contains(@id,'bp-point')])[1]")

    def select_boarding_and_dropping(self):

        wait = WebDriverWait(self.driver, 20)

        # Open boarding section
        wait.until(EC.element_to_be_clickable(self.BOARDING_SECTION)).click()
        print("✅ Boarding section opened")

        # Select boarding point
        boarding = wait.until(EC.element_to_be_clickable(self.BOARDING_POINT))
        self.driver.execute_script("arguments[0].click();", boarding)
        print("✅ Boarding point selected")

        # Select dropping point
        dropping = wait.until(EC.element_to_be_clickable(self.DROPPING_POINT))
        self.driver.execute_script("arguments[0].click();", dropping)
        print("✅ Dropping point selected")
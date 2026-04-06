from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from utils.wait_utils import WaitUtils
import time

class HomePage:

    def __init__(self, driver):
        self.driver = driver
        self.wait = WaitUtils(driver)

    FROM = (By.XPATH, "(//input[@id='srcinput'])[1]")
    TO = (By.XPATH, "//input[@id='destinput']")
    DATE = (By.XPATH, "//div[contains(@class,'dateWrapper')]")
    SEARCH = (By.XPATH, "//button[contains(text(),'Search')]")

    def enter_from(self, city):
        self.wait.send_keys(self.FROM, city)
        time.sleep(2)
        self.driver.find_element(*self.FROM).send_keys(Keys.ARROW_DOWN, Keys.ENTER)

    def enter_to(self, city):
        self.wait.send_keys(self.TO, city)
        time.sleep(2)
        self.driver.find_element(*self.TO).send_keys(Keys.ARROW_DOWN, Keys.ENTER)

    def select_date(self):
        self.wait.click(self.DATE)
        self.wait.click((By.XPATH, "//span[starts-with(@class,'doj')]"))

    def click_search(self):
        self.wait.click(self.SEARCH)
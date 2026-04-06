from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

class WaitUtils:

    def __init__(self, driver):
        self.driver = driver
        self.wait = WebDriverWait(driver, 20)

    def click(self, locator):
        self.wait.until(EC.element_to_be_clickable(locator)).click()

    def send_keys(self, locator, text):
        self.wait.until(EC.presence_of_element_located(locator)).send_keys(text)

    def get_all(self, locator):
        return self.wait.until(EC.presence_of_all_elements_located(locator))

    def js_click(self, element):
        self.driver.execute_script("arguments[0].click();", element)

    def wait_visible(self, locator):
        return self.wait.until(EC.visibility_of_element_located(locator))
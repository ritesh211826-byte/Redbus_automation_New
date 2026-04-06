from selenium.webdriver.common.by import By
from utils.wait_utils import WaitUtils

class SearchPage:

    def __init__(self, driver):
        self.driver = driver
        self.wait = WaitUtils(driver)

    VIEW = (By.XPATH, "//button[contains(text(),'View')]")

    def click_first_bus(self):
        buttons = self.wait.get_all(self.VIEW)

        self.driver.execute_script(
            "arguments[0].scrollIntoView({block:'center'});", buttons[0]
        )

        buttons[0].click()
        print("✅ Clicked View Seats")

        import time
        time.sleep(4)

        # # 🔥 ADD THIS WAIT (CRITICAL)
        # from selenium.webdriver.common.by import By
        # from selenium.webdriver.support.ui import WebDriverWait
        # from selenium.webdriver.support import expected_conditions as EC
        #
        # WebDriverWait(self.driver, 20).until(
        #     EC.visibility_of_element_located((By.XPATH, "//div[contains(@class,'seat')]"))
        # )
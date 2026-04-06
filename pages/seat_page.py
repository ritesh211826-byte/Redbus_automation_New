from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

class SeatPage:

    def __init__(self, driver):
        self.driver = driver

    # def close_popup_if_any(self):
    #     try:
    #         close_btn = WebDriverWait(self.driver, 5).until(
    #             EC.element_to_be_clickable((By.XPATH, "//button[@aria-label='Close']"))
    #         )
    #         close_btn.click()
    #         print("✅ Popup closed")
    #     except:
    #         print("ℹ️ No popup")

    def select_seat(self):

        # Wait for seat layout
        WebDriverWait(self.driver, 20).until(
            EC.visibility_of_element_located((By.XPATH, "//div[@id='leaner-funnel-popup']"))
        )

        print("✅ Seat layout loaded")

        # Wait for seats
        seats = WebDriverWait(self.driver, 20).until(
            EC.presence_of_all_elements_located((
                By.XPATH,
                "//span[contains(@style,'cursor: pointer') and not(@aria-hidden='true')]"
            ))
        )

        print(f"Seats found: {len(seats)}")


        # Click seat
        for seat in seats:
            try:
                self.driver.execute_script(
                    "arguments[0].scrollIntoView({block:'center'});", seat
                )
                self.driver.execute_script("arguments[0].click();", seat)
                print("✅ Seat selected")
                break
            except:
                continue
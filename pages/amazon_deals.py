import os
import sys
sys.path.append(os.getcwd())
from utils.common_imports import *
from utils.selenium_helpers import SeleniumHelper
from utils.logger import log_info

class TodaysDeal(SeleniumHelper):

    TODAYS_DEAL = (By.XPATH,"//a[contains(text(),\"Today's Deals\")]")
    TODAYS_DATA = (By.XPATH,"//span[contains(@class,'a-truncate-cut')]")

    @allure.step("Click on the todays deal")
    def todays_deal(self) -> None:
        self.click_element(*self.TODAYS_DEAL)

    @allure.step("Get the accessories and perform click")
    def get_deals(self) -> list:
        len_elements = 1
        i = 0
        accessories = []
        while i < len_elements:
            elements = self.get_elements(*self.TODAYS_DATA)
            for ele in elements:
                self.driver.execute_script("arguments[0].scrollIntoView();",ele)
                accessories.append(ele.text)
                len_elements = len(elements)
                if "ZEBRONICS Juke bar 9550" in ele.text:
                    log_info(f"the given value found and clicked {ele.text}")
                    ele.click()
                    self.allure_screenshot(screen_name=f"Clicked on {ele.text}")
                    break
            i += 1

        return accessories
    
    @allure.step("Store the data in file")
    def store_accesories(self):
        with open('accessories.txt', 'w') as file:
            file.write('\n'.join(self.get_deals()))
        file.close()
    

if __name__ == "__main__":
    t = TodaysDeal(driver=webdriver.Chrome())
    t.site_url("https://www.amazon.in")
    t.todays_deal()
    print(t.get_deals())
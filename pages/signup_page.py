import os
import sys
sys.path.append(os.getcwd())
from utils.common_imports import *
from pages.base_page import BasePage
from utils.logger import log_info
from config.config import *
from utils.selenium_helpers import SeleniumHelper


class SignUp_Page(SeleniumHelper):

    SIGNUP_TITLE = (By.XPATH,"//font[contains(text(),'Contact')]")
    SIGNUP_FIRST_HEAD = (By.XPATH,"//input[contains(@name,'firstName')]/preceding::b[contains(text(),'First')]")
    SIGNUP_LAST_HEAD = (By.XPATH,"//input[contains(@name,'lastName')]/preceding::b[contains(text(),'Last')]")
    SIGNUP_FIRST = (By.XPATH,"//input[contains(@name,'firstName')]")
    SIGNUP_LAST = (By.XPATH,"//input[contains(@name,'lastName')]")

    
    @allure.step("Enter the URL")
    def enter_url(self,url:str) -> None:
        self.site_url(url)


    @allure.step("Retrieve the Signup heading")
    def get_signup_head(self) -> str:
        """Fetches and logs the signup title text."""
        data = self.get_text(*self.SIGNUP_TITLE)
        log_info(f"SignUp Title : {data}")
        return data


    @allure.step("Retrieve the First Name heading")
    def get_first_title(self) -> str:
        data = self.get_text(*self.SIGNUP_FIRST_HEAD)
        log_info(f"First Name Title : {data}")
        print(f"First Name Title : {data}")

        return data
    
    @allure.step("Enter First Name")
    def enter_first_enter(self,name:str) -> None:
        self.fill_text(self.SIGNUP_FIRST, value=name)


    @allure.step("Retrieve the Last Name heading")
    def get_last_title(self) -> str:
        data = self.get_text(*self.SIGNUP_LAST_HEAD)
        log_info(f"Last Name Title : {data}")
        return data
    
    @allure.step("Enter the Last Name")
    def enter_last_enter(self,name:str) -> None:
        self.fill_text(self.SIGNUP_LAST, value=name)
        time.sleep(2)
        allure.attach(self.driver.get_screenshot_as_png(),name="SIGNUP",attachment_type=AttachmentType.PNG)
        log_info("Screenshot Taken")
    



if __name__ == "__main__":
    s = SignUp_Page(driver=webdriver.Chrome())
    s.site_url(get_url(get_url()))
    s.get_signup_head()
    s.get_first_title()
    s.enter_first_enter("Will")
    s.get_last_title()
    s.enter_last_enter("Son")
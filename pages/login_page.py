import os
import sys
sys.path.append(os.getcwd())
from utils.common_imports import *
from utils.logger import *
from config.config import *
from pages.base_page import BasePage

class Login_Page(BasePage):


    PAGE_TITLE = (By.XPATH,"//h2[contains(text(),'99')]")
    LOGIN_NAME = (By.CSS_SELECTOR,"input[name='uid']")
    LOGIN_PASS = (By.CSS_SELECTOR,"input[name='password']")
    LOGIN_BTN = (By.CSS_SELECTOR,"input[name='btnLogin']")

    @allure.step("Enter the URL")
    def enter_url(self,url:str) -> None:
        self.site_url(url)

    @allure.step("Get Title of the page")
    def get_title(self) -> Optional[str]:
        data = self.get_text(*self.PAGE_TITLE)
        log_info(f"Title of the Page is {data}")
    
    @allure.step("Enter user name")
    def enter_name(self,name) -> None:
        self.fill_text(*self.LOGIN_NAME,value=name)
        log_info(f"Username is {name}")

    @allure.step("Enter user password")
    def enter_pass(self,password) -> None:
        self.fill_text(*self.LOGIN_PASS,value=password)
        log_info(f"Password is {password}")

    @allure.step("Click on submit button")
    def click_login_btn(self) -> None:
        self.click_element(*self.LOGIN_BTN)
        log_info(f"Button clicked")

    @allure.step("Handle alert")
    def accept_alert(self):
        alert_txt = self.alert_handle_accept()
        log_info(f"the alert message is : {alert_txt}")

    

    

    


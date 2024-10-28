import os
import sys
sys.path.append(os.getcwd())
from pages.login_page import Login_Page
from utils.common_imports import *
from utils.logger import *
from data.data_helper import *


@allure.description("Check the Login page")
@allure.severity(allure.severity_level.BLOCKER)
class TestLogin:

    @pytest.fixture(scope='function',autouse=True)
    @allure.step("Login Page Setup")
    def setup_login(self):
        self.login  =Login_Page(self.driver)
    
    def test_login_url(self):
        self.login.enter_url("https://demo.guru99.com/V4/index.php")

    def test_get_title(self):
        title = self.login.get_title()
        log_info(f"the title is {title}")
    
    @pytest.mark.parametrize('username , password', (get_test_users_pass()))
    def test_enter_username(self,username,password):
        self.login.enter_name(username)
        self.login.enter_pass(password) 
        self.login.click_login_btn()
        self.login.accept_alert()
        self.login.allure_screenshot(username)
        self.driver.back()
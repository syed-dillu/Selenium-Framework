import os
import sys
sys.path.append(os.getcwd())
from pages.login_page import Login_Page
from utils.common_imports import *
from utils.logger import *
from data.data_helper import *

@allure.description("Check the Login page")
@allure.severity(allure.severity_level.BLOCKER)
@pytest.mark.order(1)
class TestLogin:


    @pytest.fixture(scope='function', autouse=True)
    def setup_login(self):
        self.login = Login_Page(self.driver) 

    @allure.severity(allure.severity_level.BLOCKER)
    @allure.title("Enter the URL")
    def test_login_url(self):
        self.login.enter_url("https://demo.guru99.com/V4/index.php")


    @allure.severity(allure.severity_level.NORMAL)
    @allure.title("Check Title of Login")
    def test_get_title(self):
        title = self.login.get_title()
        log_info(f"The title is {title}")

    @pytest.mark.parametrize('username, password', get_test_users_pass())
    @allure.severity(allure.severity_level.BLOCKER)
    @allure.title("Check Login")
    def test_enter_username(self, username, password):
        self.login.enter_name(username)
        self.login.enter_pass(password)
        self.login.click_login_btn()
        self.login.accept_alert()
        self.login.allure_screenshot(username)
        self.driver.back()

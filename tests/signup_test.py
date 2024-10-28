import os
import sys
import pytest
import allure
sys.path.append(os.getcwd())
from utils.common_imports import *
from utils.logger import *
from pages.signup_page import *
from config.config import *

@allure.description("Check the SignUp Page")
@allure.title("Sign Up")
@allure.severity(allure.severity_level.CRITICAL)
class TestSignUp:

    @pytest.fixture(scope='class', autouse=True)
    def signup_fixture(self):
        self.sign = SignUp_Page(self.driver)

    def test_enter_url(self):
        self.sign.enter_url(get_url())
        log_info(f"Enter the URL")

    def test_signup_title(self):
        data = self.sign.get_signup_head()
        log_info(f"SignUp Title Retrieved: {data}")
    
    def test_first_heading(self):
        data = self.sign.get_first_title()
        log_info(f"First Heading Retrieved: {data}")
    
    def test_enter_firstname(self):
        self.sign.enter_first_enter("sam")
        log_info("Entered First Name: sam")

    def test_last_heading(self):
        data = self.sign.get_last_title()
        log_info(f"Last Heading Retrieved: {data}")
    
    def test_enter_lastname(self):
        self.sign.enter_last_enter("Anderson")
        log_info("Entered Last Name: Anderson")
        

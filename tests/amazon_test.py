import os
import sys
sys.path.append(os.getcwd())
from utils.common_imports import *
from pages.amazon_page import AmazonPage


class TestAmazon:

    @pytest.fixture(scope='function',autouse=True)
    def setup_amazon(self):
        self.a = AmazonPage(self.driver)

    @allure.title("URL")
    def test_url(self):
        self.a.enter_url("https://www.amazon.in")
    
    @allure.title("Select Item")
    def test_select_item(self):
        self.a.select(text='Books')
    
    @allure.title("Scroll Element")
    def test_scroll(self):
        self.a.scroll()

import os
import sys
sys.path.append(os.getcwd())
from tests.conftest import flaky_test
from utils.common_imports import *
from pages.amazon_deals import TodaysDeal


@pytest.mark.order(2)
class TestTodaysDeal:


    @pytest.fixture(autouse=True)
    @allure.step("Setup: Initialize 'Today's Deals' page object")
    def setup_todays(self):
        self.t = TodaysDeal(self.driver)

    @allure.title("Verify 'Today's Deals' functionality on Amazon")
    @allure.description("Test navigates to the Amazon 'Today's Deals' page, fetches accessory data, and verifies the presence of a specific item.")
    @allure.severity(allure.severity_level.CRITICAL)
    @flaky_test(max_retries=3, delay=2)
    def test_deals(self):
        self.t.site_url("https://www.amazon.in")
        self.t.todays_deal()
    

    @allure.title("Check the scroll functionality on Amazon")
    @allure.description("Scroll to the data")
    @allure.severity(allure.severity_level.CRITICAL)
    def test_scoll_today(self):
        accessories = self.t.get_deals()
        print(accessories)
        # assert len(accessories) > 0, "No accessories found!"
        # assert "Redmi Note 13 5G" in accessories, "Specific item not found in the deals!"
    


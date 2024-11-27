import os
import sys
from utils.common_imports import *
from utils.selenium_helpers import SeleniumHelper

class AmazonPage(SeleniumHelper):

    SELECT_ELEMENT = (By.XPATH,"//select[@id = 'searchDropdownBox']")
    SCROLL_CLICK = (By.LINK_TEXT,"Mobiles")

    @allure.step("Enter the URL")
    def enter_url(self,url:str) -> None:
        self.site_url(url)

    @allure.step("Select the Element")
    def select(self,text) -> None:
        self.select_element(*self.SELECT_ELEMENT,text=text)
    
    @allure.step("Sroll Down Element")
    def scroll(self) -> None:
        self.scroll_page("window.scrollTo(0,500);")
        time.sleep(1)
        self.scroll_page("window.scrollTo(0,0);")
        self.scroll_page("window.scrollTo(0,document.body.scrollHeight);")
        self.driver.refresh()
        time.sleep(1)
        element = self.get_element(*self.SCROLL_CLICK)
        self.scroll_element("arguments[0].scrollIntoView();",element)
        time.sleep(1)

        self.scroll_element("arguments[0].click();",element)



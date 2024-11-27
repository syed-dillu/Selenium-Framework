import os
import sys
sys.path.append(os.getcwd())
from utils.common_imports import *
from config.config import get_expilicitwait

class BasePage:

    def __init__(self,driver:Union[webdriver.Chrome,webdriver.Firefox,webdriver.Edge]):
        self.driver = driver
        self.wait = WebDriverWait(self.driver,get_expilicitwait())

    def site_url(self,url:str) -> None:
        self.driver.get(url)
    
    def quit_browser(self) -> None:
        self.driver.quit()
    
    def close_browser(self) -> None:
        self.driver.close()

if __name__ == "__main__":
    BasePage(driver=webdriver.Chrome())
import os
import sys
sys.path.append(os.getcwd())
from utils.logger import *
from utils.common_imports import *
from config.config import *

class BasePage:

    def __init__(self,driver:Union[webdriver.Chrome,webdriver.Firefox,webdriver.Edge]):
        self.driver = driver
        self.wait = WebDriverWait(self.driver,get_expilicitwait())

    def site_url(self,url:str) -> None:
        self.driver.get(url)
    
    def fill_text(self, *locator : tuple, value : str) -> None:
        try:
            element : WebElement = self.wait.until(EC.visibility_of_element_located(locator))
            element.send_keys(value)
        except Exception as e:
            log_error(f"Error Filling text on a element {locator} : {str(e)}")
            

    def click_element(self, *locator : tuple) -> None:
        try:
            element : WebElement = self.wait.until(EC.element_to_be_clickable(locator))
            element.click()
        except Exception as e:
            log_error(f"Error Clicking on the element {locator} : {str(e)}")
    
    def get_element(self, *locator: tuple) -> Optional[WebElement] :
        try:
            element : WebElement = self.wait.until(EC.visibility_of_element_located(locator))
            return element
        except Exception as e:
            log_error(f"Error at retrieving the element {locator} : {str(e)}")
            return None

    def get_elements(self, *locator: tuple) -> list[WebElement] :
        try:
            element : WebElement = self.wait.until(EC.presence_of_all_elements_located(locator))
            return element
        except Exception as e:
            log_error(f"Error at retrieving all the elements {locator} : {str(e)}")  
            return []
    
    def get_text(self, *locator: tuple) -> Optional[str] :
        try:
            element : WebElement = self.wait.until(EC.visibility_of_element_located(locator))
            return element.text
        except Exception as e:
            log_error(f"Error at retrieving text of the element {locator} : {str(e)}")
            return None
        
    def quit_browser(self) -> None:
        self.driver.quit()
    
    def close_browser(self) -> None:
        self.driver.close()
    
    def allure_screenshot(self, screen_name) -> None:
        time.sleep(1)
        allure.attach(self.driver.get_screenshot_as_png(),name=screen_name,attachment_type=AttachmentType.PNG)
        log_info("Screenshot Retrieved")
    
    def alert_handle_accept(self):
        alert = self.wait.until(EC.alert_is_present())
        try:
            time.sleep(1)
            alert_text = alert.text
            alert.accept()
            return alert_text
        except Exception as e:
            log_error(f"Error at Handle the alert {str(e)}")

    
    

if __name__ == "__main__":
    BasePage()
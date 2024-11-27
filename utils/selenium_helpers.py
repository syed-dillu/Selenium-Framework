import os
import sys
from typing import List
from datetime import datetime
from pathlib import Path
sys.path.append(os.getcwd())
from utils.common_imports import *
from pages.base_page import BasePage
from utils.logger import log_error, log_info, store_screenshot


class SeleniumHelper(BasePage):

    def fill_text(self, locator: tuple, value: str) -> None:
        """Fill the text box field using visibility"""
        try:
            element: WebElement = self.wait.until(EC.visibility_of_element_located(locator))
            element.clear()
            element.send_keys(value)
            self.allure_screenshot(screen_name=value)

        except Exception as e:
            screens = store_screenshot()
            self.driver.save_screenshot(screens)
            self.allure_screenshot(screen_name=value)
            log_error(f"Error filling text in the element {locator}: {str(e)}. Screenshot saved at {screens}")
            pytest.fail(f"Error filling text in the element {locator}: {str(e)}. Check screenshot at {screens}")

    def click_element(self, *locator: tuple) -> None:
        """Click on the web element using clickable"""
        try:
            element: WebElement = self.wait.until(EC.element_to_be_clickable(locator))
            element.click()
        except Exception as e:
            screens = store_screenshot()
            self.driver.save_screenshot(screens)
            self.allure_screenshot(screen_name=locator[1])
            log_error(f"Error clicking on the element {locator}: {str(e)}. Screenshot saved at {screens}")
            pytest.fail(f"Error clicking on the element {locator}: {str(e)}. Check screenshot at {screens}")

    def get_element(self, *locator: tuple) -> WebElement:
        """Get the web element using visibility"""
        try:
            element: WebElement = self.wait.until(EC.visibility_of_element_located(locator))
            return element
        except Exception as e:
            screens = store_screenshot()
            self.driver.save_screenshot(screens)
            log_error(f"Error retrieving the element {locator}: {str(e)}. Screenshot saved at {screens}")
            pytest.fail(f"Error retrieving the element {locator}: {str(e)}. Check screenshot at {screens}")
            self.allure_screenshot(screen_name=locator[1])

    def get_elements(self, *locator: tuple) -> List[WebElement]:
        """Get the web elements using presence"""
        try:
            elements: List[WebElement] = self.wait.until(EC.presence_of_all_elements_located(locator))
            return elements
        except Exception as e:
            screens = store_screenshot()
            self.driver.save_screenshot(screens)
            log_error(f"Error retrieving all elements {locator}: {str(e)}. Screenshot saved at {screens}")
            pytest.fail(f"Error retrieving all elements {locator}: {str(e)}. Check screenshot at {screens}")
            self.allure_screenshot(screen_name=locator[1])

    def get_text(self, *locator: tuple) -> str:
        """Get the text of the web element using visibility"""
        try:
            element: WebElement = self.wait.until(EC.visibility_of_element_located(locator))
            return element.text
        except Exception as e:
            screens = store_screenshot()
            self.driver.save_screenshot(screens)
            log_error(f"Error retrieving text of the element {locator}: {str(e)}. Screenshot saved at {screens}")
            pytest.fail(f"Error retrieving text of the element {locator}: {str(e)}. Check screenshot at {screens}")
            self.allure_screenshot(screen_name=locator[1])

    def allure_screenshot(self, screen_name: str) -> None:
        """Capture screenshot using Allure"""
        try:
            time.sleep(1)
            allure.attach(
                self.driver.get_screenshot_as_png(),
                name=screen_name,
                attachment_type=AttachmentType.PNG
            )
            log_info("Screenshot captured")
        except Exception as e:
            log_error(f"Error capturing screenshot: {str(e)}")
            pytest.fail(f"Error capturing screenshot: {str(e)}")

    def alert_handle_accept(self) -> str:
        """Handle JavaScript alerts and accept them"""
        try:
            alert = self.wait.until(EC.alert_is_present())
            time.sleep(1)
            alert_text = alert.text
            alert.accept()
            return alert_text
        except Exception as e:
            screens = store_screenshot()
            self.driver.save_screenshot(screens)
            log_error(f"Error handling the alert: {str(e)}. Screenshot saved at {screens}")
            pytest.fail(f"Error handling the alert: {str(e)}. Check screenshot at {screens}")
            self.allure_screenshot(screen_name="alert")

    def select_element(self, *locator: tuple, text: str) -> None:
        """Select an option from a dropdown by visible text"""
        try:
            element: WebElement = self.driver.find_element(*locator)
            select = Select(element)
            select.select_by_visible_text(text)
        except Exception as e:
            screens = store_screenshot()
            self.driver.save_screenshot(screens)
            log_error(f"Error selecting the element {locator}: {str(e)}. Screenshot saved at {screens}")
            pytest.fail(f"Error selecting the element {locator}: {str(e)}. Check screenshot at {screens}")
            self.allure_screenshot(screen_name=locator[1])

    def scroll_element(self, script: str, element: WebElement) -> None:
        """Scroll to a specific element using JavaScript"""
        try:
            self.driver.execute_script(script, element)
        except Exception as e:
            screens = store_screenshot()
            self.driver.save_screenshot(screens)
            log_error(f"Error scrolling to the element: {str(e)}. Screenshot saved at {screens}")
            pytest.fail(f"Error scrolling to the element: {str(e)}. Check screenshot at {screens}")
            self.allure_screenshot(screen_name=element)

    def scroll_page(self, script: str) -> None:
        """Scroll the page using JavaScript"""
        try:
            self.driver.execute_script(script)
        except Exception as e:
            screens = store_screenshot()
            self.driver.save_screenshot(screens)
            log_error(f"Error scrolling the page: {str(e)}. Screenshot saved at {screens}")
            pytest.fail(f"Error scrolling the page: {str(e)}. Check screenshot at {screens}")
            self.allure_screenshot(screen_name=f"failed at scroll")

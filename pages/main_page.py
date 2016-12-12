from selenium.webdriver.support.ui import WebDriverWait
from selenium.common.exceptions import TimeoutException
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import NoSuchElementException
import time
from basepage import BasePage

class MainPage(BasePage):
    WRITE_REVIEW_BUTTON = {"by": By.XPATH, "value": "//span[contains(., 'Write a review')]"}

    def click_write_review(self):
        self.driver.find_element(self.WRITE_REVIEW_BUTTON['by'],self.WRITE_REVIEW_BUTTON['value'] ).click()

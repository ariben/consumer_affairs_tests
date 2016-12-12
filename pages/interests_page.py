from selenium.webdriver.support.ui import WebDriverWait
from selenium.common.exceptions import TimeoutException
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import NoSuchElementException
from basepage import BasePage
from selenium.webdriver.support.ui import Select

class InterestsPage(BasePage):
    DONE_BUTTON = {"by": By.XPATH, "value": "//input[@value='Done']"}

    def click_done(self):
        self.driver.find_element(self.DONE_BUTTON['by'],self.DONE_BUTTON['value'] ).click()

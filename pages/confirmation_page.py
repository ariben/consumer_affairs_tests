from selenium.webdriver.support.ui import WebDriverWait
from selenium.common.exceptions import TimeoutException
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import NoSuchElementException
from basepage import BasePage
from selenium.webdriver.support.ui import Select

class ConfirmationPage(BasePage):
    CONTINUE_WITH_REVIEW_BUTTON = {"by": By.LINK_TEXT, "value": "Continue with my review"}

    def continue_with_review(self):
        self.driver.find_element(self.CONTINUE_WITH_REVIEW_BUTTON['by'],self.CONTINUE_WITH_REVIEW_BUTTON['value'] ).click()

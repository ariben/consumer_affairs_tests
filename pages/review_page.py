from selenium.webdriver.support.ui import WebDriverWait
from selenium.common.exceptions import TimeoutException
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import NoSuchElementException
import time
from basepage import BasePage

class ReviewPage(BasePage):
    CREATE_ACCOUNT_BUTTON = {"by": By.LINK_TEXT, "value": "Create account"}

    def create_account(self):
        self.driver.find_element(self.CREATE_ACCOUNT_BUTTON["by"],self.CREATE_ACCOUNT_BUTTON["value"]).click()

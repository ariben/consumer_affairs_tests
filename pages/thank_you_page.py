from selenium.webdriver.support.ui import WebDriverWait
from selenium.common.exceptions import TimeoutException
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import NoSuchElementException
import time
from basepage import BasePage
from selenium.webdriver.support.ui import Select

class ThankYouPage(BasePage):
    WRITE_REVIEW_BUTTON = {"by": By.LINK_TEXT, "value": "Write a review"}

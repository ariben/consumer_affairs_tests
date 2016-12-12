from selenium.webdriver.support.ui import WebDriverWait
from selenium.common.exceptions import TimeoutException
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import NoSuchElementException
import time
from basepage import BasePage

class CreateAccountPage(BasePage):
    EMAIL_ADDRESS_TEXTBOX = {"by": By.ID, "value": "id_email"}
    EMAIL_ADDRESS_TEXTBOX2 = {"by": By.ID, "value": "id_email2"}
    PASSWORD_ADDRESS_TEXTBOX = {"by": By.ID, "value": "id_password1"}
    PASSWORD_ADDRESS_TEXTBOX2 = {"by": By.ID, "value": "id_password2"}
    CONTINUE_BUTTON = {"by": By.XPATH, "value": "//button[text()='Continue']"}

    def input_value(self, element, value):
        textbox = self.driver.find_element(element["by"], element["value"])
        textbox.send_keys(value)

    def input_account_values(self, user_email, user_email2, user_password,user_password2):
        self.input_value(self.EMAIL_ADDRESS_TEXTBOX, user_email)
        self.input_value(self.EMAIL_ADDRESS_TEXTBOX2, user_email2)
        self.input_value(self.PASSWORD_ADDRESS_TEXTBOX, user_password)
        self.input_value(self.PASSWORD_ADDRESS_TEXTBOX2 , user_password2)

    def continue_with_account_creation(self):
        self.driver.find_element(self.CONTINUE_BUTTON["by"],self.CONTINUE_BUTTON["value"] ).click()

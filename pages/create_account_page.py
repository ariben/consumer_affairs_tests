from selenium.webdriver.support.ui import WebDriverWait
from selenium.common.exceptions import TimeoutException
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import NoSuchElementException
import time
from pages.basepage import BasePage

class CreateAccountPage(BasePage):
    FIRST_NAME_TEXTBOX = {"by": By.ID, "value": "id_first_name"}
    LAST_NAME_TEXTBOX = {"by": By.ID, "value": "id_last_name"}
    STREET_ADDRESS_TEXTBOX = {"by": By.ID, "value": "id_address"}
    ZIP_TEXTBOX = {"by": By.ID, "value": "id_zip"}
    COUNTRY_LIST = {"by": By.CLASS_NAME, "value": "choices__inner"}
    COUNTRY_INPUT = {"by": By.CLASS_NAME, "value": "choices__input"}

    EMAIL_ADDRESS_TEXTBOX = {"by": By.ID, "value": "id_email"}
    PASSWORD_TEXTBOX = {"by": By.ID, "value": "id_password1"}
    PASSWORD_TEXTBOX2 = {"by": By.ID, "value": "id_password2"}
    CAPTCHA_BUTTON = {"by" : By.CLASS_NAME, "value": "recaptcha-checkbox-border"}
    CREATE_ACCOUNT_BUTTON = {"by": By.XPATH, "value": "//button[contains(text(), 'Create account')]"}

    def input_value(self, element, value):
        textbox = self.driver.find_element(element["by"], element["value"])
        textbox.send_keys(value)

    def input_account_values(self,firstname, lastname, phone_number, address, zipcode, country, user_email, user_password, user_password2):
        self.input_value(self.FIRST_NAME_TEXTBOX, firstname)
        self.input_value(self.LAST_NAME_TEXTBOX, lastname)
        self.input_value(self.STREET_ADDRESS_TEXTBOX , address)
        self.input_value(self.EMAIL_ADDRESS_TEXTBOX, user_email)
        self.input_value(self.PASSWORD_TEXTBOX, user_password)
        self.input_value(self.PASSWORD_TEXTBOX2 , user_password)

    def create_acccount(self):
        self.driver.find_element(self.CREATE_ACCOUNT_BUTTON["by"],self.CREATE_ACCOUNT_BUTTON["value"] ).click()

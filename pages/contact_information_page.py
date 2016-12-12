from selenium.webdriver.support.ui import WebDriverWait
from selenium.common.exceptions import TimeoutException
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import NoSuchElementException
import time
from basepage import BasePage
from selenium.webdriver.support.ui import Select

class ContactInformationPage(BasePage):
    FIRST_NAME_TEXTBOX = {"by": By.ID, "value": "id_first_name"}
    LAST_NAME_TEXTBOX = {"by": By.ID, "value": "id_last_name"}
    PHONE_TEXTBOX = {"by": By.ID, "value": "id_phone"}
    STREET_ADDRESS1_TEXTBOX = {"by": By.ID, "value": "id_address"}
    STREET_ADDRESS2_TEXTBOX = {"by": By.ID, "value": "id_address2"}
    CITY_TEXTBOX = {"by": By.ID, "value": "id_city"}
    ZIP_TEXTBOX = {"by": By.ID, "value": "id_zip"}
    COUNTRY_LIST = {"by": By.ID, "value": "id_country"}
    NEWSLETTER_CHECKBOX = {"by": By.ID, "value": "id_newsletter"}
    CREATE_ACCOUNT_BUTTON = {"by": By.XPATH, "value": "//button[text()='Create account']"}

    def select_from_list(self, element, value):
        select = Select(self.driver.find_element(element["by"], element["value"]))
        select.select_by_value(value)


    def input_value(self, element, value):
        textbox = self.driver.find_element(element["by"], element["value"])
        textbox.send_keys(value)

    def input_profile_details(self,firstname, lastname, phone_number, address1, address2, city, zipcode, country, subscribe_newsletter = True):
        self.input_value(self.FIRST_NAME_TEXTBOX, firstname)
        self.input_value(self.LAST_NAME_TEXTBOX, lastname)
        self.input_value(self.PHONE_TEXTBOX, phone_number)
        self.input_value(self.STREET_ADDRESS1_TEXTBOX, address1)
        self.input_value(self.STREET_ADDRESS2_TEXTBOX, address2)
        self.input_value(self.CITY_TEXTBOX, city)
        self.input_value(self.ZIP_TEXTBOX, zipcode)
        self.select_from_list(self.COUNTRY_LIST, country)
        if subscribe_newsletter == False:
            self.driver.find_element(self.NEWSLETTER_CHECKBOX["by"], self.NEWSLETTER_CHECKBOX["value"]).click()


    def click_create_account(self):
        self.driver.find_element(self.CREATE_ACCOUNT_BUTTON["by"], self.CREATE_ACCOUNT_BUTTON["value"]).click()

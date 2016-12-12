from selenium.webdriver.support.ui import WebDriverWait
from selenium.common.exceptions import TimeoutException
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import NoSuchElementException
from basepage import BasePage
from selenium.webdriver.support.ui import Select
import time

class WriteReviewPage(BasePage):
    BUSINESS_TEXTBOX = {"by": By.ID, "value": "id_org-name"}
    DEPARTMENT_TEXTBOX = {"by": By.ID, "value": "id_org-company_contact"}
    REVIEW_SUBJECT_TEXTBOX = {"by": By.ID, "value": "id_review_text-subject"}
    REVIEW_EXPERIENCE_TEXTBOX = {"by": By.ID, "value": "id_review_text-description"}
    ORDER_NUMBER_TEXTBOX = {"by": By.ID, "value": "id_review-order_number"}
    #TODO: All other elements on page
    STAR_REVIEW= {"by": By.CLASS_NAME, "value": "ui-stars-star"}
    CERTIFY_CHECKBOX = {"by": By.ID, "value": "id_review-solicited_review"}
    SUBMIT_REVIEW_BUTTON = {"by": By.ID, "value": "submit_review"}

    def input_value(self, element, value):
        textbox = self.driver.find_element(element["by"], element["value"])
        textbox.send_keys(value)


    def input_review(self, organization_name, department, subject, experience, number_stars):
        self.input_value(self.BUSINESS_TEXTBOX, organization_name)
        self.input_value(self.DEPARTMENT_TEXTBOX, department)
        self.input_value(self.REVIEW_SUBJECT_TEXTBOX, subject)
        self.input_value(self.REVIEW_EXPERIENCE_TEXTBOX, experience)
        stars = self.driver.find_elements(self.STAR_REVIEW["by"], self.STAR_REVIEW["value"])
        stars[number_stars - 1].click()

    def certify_review(self):
        self.driver.find_element(self.CERTIFY_CHECKBOX['by'],self.CERTIFY_CHECKBOX['value'] ).click()

    def submit_review(self):
        self.driver.find_element(self.SUBMIT_REVIEW_BUTTON['by'],self.SUBMIT_REVIEW_BUTTON['value'] ).click()

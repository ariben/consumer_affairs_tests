import unittest
from datetime import datetime

#custom imports
import sys,site
from basetest import BaseTest
from pages import main_page as mainpage
from pages import review_page as reviewpage
from pages import create_account_page as createaccountpage
from pages import contact_information_page as contactinfopage
from pages import interests_page as interestspage
from pages import confirmation_page as confirmationpage
from pages import write_review_page as writereviewpage
from utils import HTMLTestRunner, utilities
import time


class ReviewTests(BaseTest):

    def test_write_review_succesful(self):
        main_page = mainpage.MainPage(self.driver)
        main_page.click_write_review()
        review_page = reviewpage.ReviewPage(self.driver)
        expected_text = "Let's get started"
        assert review_page.has_text(expected_text), "Expected text <%s> was not displayed"
        review_page.create_account()
        create_account_page = createaccountpage.CreateAccountPage(self.driver)
        expected_text = "Create your account"
        assert create_account_page.has_text(expected_text), "Expected text <%s> was not displayed"
        user_mail = "%s@mail.com" % utilities.string_generator()
        user_password = utilities.string_generator()
        create_account_page.input_account_values(user_mail, user_mail, user_password, user_password)
        create_account_page.continue_with_account_creation()
        contact_information_page = contactinfopage.ContactInformationPage(self.driver)
        expected_text = "Create an account"
        assert contact_information_page.has_text(expected_text), "Expected text <%s> was not displayed"
        contact_information_page.input_profile_details(firstname=utilities.string_generator(), lastname=utilities.string_generator(),
                                                        phone_number='55111578',address1=utilities.string_generator(),
                                                        address2=utilities.string_generator(), city=utilities.string_generator(),
                                                        zipcode='lima 12', country= "Peru", subscribe_newsletter = False)
        contact_information_page.click_create_account()
        interests_page = interestspage.InterestsPage(self.driver)
        interests_page.click_done()
        confirmation_page = confirmationpage.ConfirmationPage(self.driver)
        confirmation_page.continue_with_review()
        write_review_page = writereviewpage.WriteReviewPage(self.driver)
        write_review_page.input_review(organization_name=utilities.string_generator(), department=utilities.string_generator(),
                                        subject=utilities.string_generator(), experience=utilities.string_generator(), number_stars = 1)
        write_review_page.certify_review()
        write_review_page.submit_review()
        time.sleep(10)



if __name__ == "__main__":
    suite = unittest.TestSuite()
    suite.addTest(unittest.makeSuite(ReviewTests))
    filename = "reports/ReviewsTestsReport_%s_.html" % datetime.now().strftime('%Y-%m-%d_%H-%M-%S')
    fp = file(filename, 'wb')
    runner = HTMLTestRunner.HTMLTestRunner(
                stream=fp,
                title='Write Reviews Tests',
                description='Test Report on Review Tests'
                )
    runner.run(suite)

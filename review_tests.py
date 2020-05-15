import unittest
from datetime import datetime

#custom imports
import sys,site
from basetest import BaseTest
from pages import main_page as mainpage
from pages import review_page as reviewpage
from pages import create_account_page as createaccountpage
from utils import HTMLTestRunner, utilities
import time


class ReviewTests(BaseTest):

    def test_write_review_succesful(self):
        main_page = mainpage.MainPage(self.driver)
        main_page.click_write_review()
        time.sleep(3)
        review_page = reviewpage.ReviewPage(self.driver)
        expected_text = "How would you like to share your experience?"
        assert review_page.has_text(expected_text), "Expected text <%s> was not displayed"
        review_page.write_review()
        time.sleep(3)
        create_account_page = createaccountpage.CreateAccountPage(self.driver)
        expected_text = "Create your account"
        assert create_account_page.has_text(expected_text), "Expected text <%s> was not displayed"
        user_mail = "%s@mail.com" % utilities.string_generator()
        user_password = utilities.string_generator(8, '98axxAA$(M')
        create_account_page.input_account_values(firstname=utilities.string_generator(), lastname=utilities.string_generator(),
                                                phone_number='12345678901',address=utilities.string_generator(),
                                                zipcode='90201', country= "Peru", user_email=user_mail, user_password = user_password,user_password2=user_password)
        create_account_page.create_acccount()
        assert review_page.has_text("required"), "Expected text <%s> was not displayed"
        time.sleep(5)



if __name__ == "__main__":
    suite = unittest.TestSuite()
    suite.addTest(unittest.makeSuite(ReviewTests))
    filename = "reports/ReviewsTestsReport_%s_.html" % datetime.now().strftime('%Y-%m-%d_%H-%M-%S')
    fp = open(filename, 'wb')
    runner = HTMLTestRunner.HTMLTestRunner(
                stream=fp,
                title='Write Reviews Tests',
                description='Test Report on Review Tests'
                )
    runner.run(suite)

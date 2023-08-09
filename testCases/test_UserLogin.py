import allure
import pytest
from allure_commons.types import AttachmentType

from pageObject.UserLoginPage import UserLoginClass
from pageObject.UserRegistrationPage import UserRegistrationClass
from utilities.Logger import LogGen
from utilities.ReadConfigFile import ReadConfig


class TestLogin:
    log = LogGen.loggen()
    username = ReadConfig.get_username()
    password = ReadConfig.get_password()

    @allure.severity(allure.severity_level.CRITICAL)
    @pytest.mark.regression
    def test_login_002(self, setup):
        self.log.info("Testcase test_login_002 is started")
        self.driver = setup
        self.log.info("Invoking the browser")
        self.log.info("Opening the Url")
        self.lp = UserLoginClass(self.driver)
        self.lp.link_login()
        self.log.info("Clicking on login link")
        self.lp.email_id(self.username)
        self.log.info("Entering the username -->" + self.username)
        self.lp.password(self.password)
        self.log.info("Entering the password -->" + self.password)
        self.lp.login_btn()
        self.log.info("Clicking on login button")
        self.rp = UserRegistrationClass(self.driver)

        if self.rp.status():
            self.log.info("TestCase test_login_002 is Passed ")
            self.driver.save_screenshot(".\\Screenshots\\test_login_002_pass.png")
            assert True
        else:
            self.log.info("TestCase test_login_002 is Failed ")
            self.driver.save_screenshot(".\\Screenshots\\test_login_002_fail.png")
            allure.attach(self.driver.get_screenshot_as_png(), name="test_login_002",
                          attachment_type=AttachmentType.PNG)
            assert False
        self.driver.close()
        self.log.info("TestCase test_login_002 is Completed")



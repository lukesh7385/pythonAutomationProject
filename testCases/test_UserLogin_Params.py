import allure
import pytest
from allure_commons.types import AttachmentType

from pageObject.UserLoginPage import UserLoginClass
from pageObject.UserRegistrationPage import UserRegistrationClass
from utilities.Logger import LogGen
from utilities.ReadConfigFile import ReadConfig


class TestLoginParams:
    log = LogGen.loggen()
    baseURL = ReadConfig.get_application_url()

    @allure.severity(allure.severity_level.CRITICAL)
    @pytest.mark.regression
    def test_login_params_003(self, setup, data_for_login):
        self.log.info("TestCases test_login_params_003 is stared")
        self.driver = setup
        self.driver.get(self.baseURL)
        self.log.info("Invoking browser")
        self.log.info("Navigating to Url")
        self.lp = UserLoginClass(self.driver)
        self.lp.link_login()
        self.log.info("Clicking on login link")
        self.lp.email_id(data_for_login[0])
        self.log.info("Entering Email -->" + data_for_login[0])
        self.lp.password(data_for_login[1])
        self.log.info("Entering Password-->" + data_for_login[1])
        self.lp.login_btn()
        self.log.info("Clicking on login button")
        self.rp = UserRegistrationClass(self.driver)
        if self.rp.status() == (data_for_login[2] == "Pass"):
            self.log.info("TestCases test_login_params_003 is Passed")
            self.driver.save_screenshot(".\\Screenshots\\test_login_params_003_passed.png")
            assert True
        else:
            self.log.info("TestCases test_login_params_003 is Failed")
            allure.attach(self.driver.get_screenshot_as_png(), name="test_login_params_003",
                          attachment_type=AttachmentType.PNG)
            self.driver.save_screenshot(".\\Screenshots\\test_login_params_003_failed.png")
            assert False
        self.driver.close()
        self.log.info("TestCases test_login_003 is completed")

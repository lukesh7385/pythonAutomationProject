import allure
import pytest
from allure_commons.types import AttachmentType

from pageObject.UserRegistrationPage import UserRegistrationClass
from utilities.Logger import LogGen
from utilities.ReadConfigFile import ReadConfig


class TestRegistration:
    log = LogGen.loggen()
    password = ReadConfig.get_password()
    baseURL = ReadConfig.get_application_url()

    @allure.severity(allure.severity_level.CRITICAL)
    @pytest.mark.sanity
    def test_registration_001(self, setup):
        self.log.info("TestCase test_registration_001 is started")
        self.driver = setup
        self.driver.get(self.baseURL)
        self.log.info("Invoking the browser")
        self.log.info("Opening URL")
        self.rp = UserRegistrationClass(self.driver)
        self.rp.link_registration()
        self.log.info("Clicking on registration link")
        self.rp.name("lukesh")
        self.log.info("Entering name")
        self.rp.email(self.rp.generate_random_username() + "@credence.in")
        self.log.info("Entering Email")
        self.rp.password(self.password)
        self.log.info("Entering password")
        self.rp.confirm_password(self.password)
        self.log.info("Conforming password")
        self.rp.btn_register()
        self.log.info("Clicking on registration button")

        if self.rp.status():
            self.log.info("TestCase test_registration_001 is Passed")
            self.driver.save_screenshot(".\\Screenshots\\test_registration_001_pass.png")
            assert True
        else:
            self.log.info("TestCase test_registration_001 is Failed")
            allure.attach(self.driver.get_screenshot_as_png(), name="test_registration_001",
                          attachment_type=AttachmentType.PNG)
            self.driver.save_screenshot(".\\Screenshots\\test_registration_001_fail.png")
            assert False
        self.driver.close()
        self.log.info("TestCase test_registration_001 is completed")

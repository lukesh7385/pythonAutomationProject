import allure
import pytest
from allure_commons.types import AttachmentType

from pageObject.UserLoginPage import UserLoginClass
from pageObject.UserRegistrationPage import UserRegistrationClass
from utilities import XLutilites
from utilities.Logger import LogGen
from utilities.ReadConfigFile import ReadConfig


class TestLoginDDT:
    username = ReadConfig.get_username()
    password = ReadConfig.get_password()
    log = LogGen.loggen()
    path = ".\\testCases\\TestData\\LoginData.xlsx"

    @allure.severity(allure.severity_level.CRITICAL)
    @pytest.mark.regression
    def test_login_ddt_003(self, setup):
        self.log.info("TestCase test_login_DDT_003 is started")
        self.driver = setup
        self.log.info("Invoking browser")
        self.log.info("Navigating to URL")
        self.lp = UserLoginClass(self.driver)
        self.rows = XLutilites.getRowCount(self.path, "Sheet1")
        login_status = []
        for r in range(2, self.rows + 1):
            self.username = XLutilites.readData(self.path, "Sheet1", r, 1)
            self.password = XLutilites.readData(self.path, "Sheet1", r, 2)
            self.exp_result = XLutilites.readData(self.path, "Sheet1", r, 3)
            self.lp.link_login()
            self.log.info("Clicking on login link")
            self.lp.email_id(self.username)
            self.log.info("Entering email id-->" + self.username)
            self.lp.password(self.password)
            self.log.info("Entering password-->" + self.password)
            self.lp.login_btn()
            self.log.info("Clicking on login button")
            self.rp = UserRegistrationClass(self.driver)

            if self.rp.status():
                if self.exp_result == "Pass":
                    login_status.append("Pass")
                    XLutilites.writeData(self.path, "Sheet1", r, 4, "Pass")
                    self.driver.save_screenshot(".\\Screenshots\\test_login_DDT_003_pass.png")
                    self.lp.logout_btn()
                elif self.exp_result == "Fail":
                    login_status.append("Fail")
                    XLutilites.writeData(self.path, "Sheet1", r, 4, "Fail")
                    self.driver.save_screenshot(".\\Screenshots\\test_login_DDT_003_pass.png")
                    self.lp.logout_btn()
            elif not self.rp.status():
                if self.exp_result == "Pass":
                    login_status.append("Fail")
                    XLutilites.writeData(self.path, "Sheet1", r, 4, "Fail")
                    self.driver.refresh()
                    self.driver.save_screenshot(".\\Screenshots\\test_login_DDT_003_fail.png")
                elif self.exp_result == "Fail":
                    login_status.append("Pass")
                    XLutilites.writeData(self.path, "Sheet1", r, 4, "Pass")
                    self.driver.refresh()
                    self.driver.save_screenshot(".\\Screenshots\\test_login_DDT_003_fail.png")

        if 'Fail' not in login_status:
            self.log.info("TestCases test_login_DDT_003 is passed")
            self.driver.close()
            assert True
        else:
            self.log.info("TestCases test_login_DDT_003 is failed")
            allure.attach(self.driver.get_screenshot_as_png(), name="test_login_ddt_003",
                          attachment_type=AttachmentType.PNG)
            self.driver.close()
            assert False

        self.log.info("********* End of Login DDT Test *********")

        self.log.info("************** Completed TestCase test_login_DDT_003 **************")

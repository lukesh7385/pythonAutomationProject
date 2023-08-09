import allure
import pytest
from allure_commons.types import AttachmentType

from pageObject.UserLoginPage import UserLoginClass
from pageObject.UserRegistrationPage import UserRegistrationClass
from utilities import XLutilites
from utilities.Logger import LogGen
from utilities.ReadConfigFile import ReadConfig


class TestLoginDDT:
    baseURL = ReadConfig.get_application_url()
    username = ReadConfig.get_username()
    password = ReadConfig.get_password()
    log = LogGen.loggen()
    path = ".\\testCases\\TestData\\LoginData.xlsx"

    @allure.severity(allure.severity_level.CRITICAL)
    @pytest.mark.regression
    def test_login_ddt_003(self, setup):
        self.log.info("TestCase test_login_DDT_003 is started")
        self.log.info("verifying Login DDT test")
        self.driver = setup
        self.driver.get(self.baseURL)
        self.log.info("Invoking browser")
        self.log.info("Navigating to URL")

        self.lp = UserLoginClass(self.driver)
        self.rows = XLutilites.getRowCount(self.path, "Sheet1")
        list_status = []  # Empty list variable

        for r in range(2, self.rows + 1):
            try:
                self.username = XLutilites.readData(self.path, 'Sheet1', r, 1)
                self.password = XLutilites.readData(self.path, 'Sheet1', r, 2)
                self.exp_result = XLutilites.readData(self.path, 'Sheet1', r, 3)
            except Exception as e:
                self.log.error(f"An error occurred in row {r}: {e}")

            if self.username is not None and self.password is not None:
                self.log.info(f"Login status after iteration {r}: {list_status}")

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
                if self.exp_result == 'Pass':
                    list_status.append('Pass')
                    XLutilites.writeData(self.path, "Sheet1", r, 4, 'Pass')
                    self.driver.save_screenshot(".\\Screenshots\\test_login_DDT_003_pass.png")
                    self.lp.logout_btn()
                elif self.exp_result == 'Fail':
                    list_status.append('Fail')
                    XLutilites.writeData(self.path, "Sheet1", r, 4, 'Fail')
                    self.driver.save_screenshot(".\\Screenshots\\test_login_DDT_003_pass.png")
                    self.lp.logout_btn()
            elif not self.rp.status():
                if self.exp_result == 'Pass':
                    list_status.append('Fail')
                    XLutilites.writeData(self.path, "Sheet1", r, 4, 'Fail')
                    self.driver.save_screenshot(".\\Screenshots\\test_login_DDT_003_fail.png")
                    self.driver.refresh()
                elif self.exp_result == 'Fail':
                    list_status.append('Pass')
                    XLutilites.writeData(self.path, "Sheet1", r, 4, 'Pass')
                    self.driver.save_screenshot(".\\Screenshots\\test_login_DDT_003_Pass.png")
                    self.driver.refresh()

        if 'Fail' not in list_status:
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

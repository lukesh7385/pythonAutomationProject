import time

from selenium.webdriver.common.by import By


class UserLoginClass:
    clickOnLoginLink_LINK_TEXT = (By.LINK_TEXT, "Login")
    textEmail_ID = (By.ID, "email")
    textPassword_NAME = (By.NAME, "password")
    btnLongin_XPATH = (By.XPATH, "//button[normalize-space()='Login']")
    linkLogout_XPATH = (By.XPATH, "//a[@role='button']")
    btnLogout_XPATH = (By.XPATH, "//a[normalize-space()='Logout']")

    def __init__(self, driver):
        self.driver = driver

    def link_login(self):
        self.driver.find_element(*UserLoginClass.clickOnLoginLink_LINK_TEXT).click()

    def email_id(self, mail):
        self.driver.find_element(*UserLoginClass.textEmail_ID).send_keys(mail)

    def password(self, password):
        self.driver.find_element(*UserLoginClass.textPassword_NAME).send_keys(password)

    def login_btn(self):
        self.driver.find_element(*UserLoginClass.btnLongin_XPATH).click()

    def logout_btn(self):
        self.driver.find_element(*UserLoginClass.linkLogout_XPATH).click()
        self.driver.find_element(*UserLoginClass.btnLogout_XPATH).click()

import random
import string

from selenium.common import NoSuchElementException
from selenium.webdriver.common.by import By


class UserRegistrationClass:
    linkRegistration_LinkText = (By.LINK_TEXT, "Register")
    textName_NAME = (By.NAME, "name")
    textEmail_id = (By.ID, "email")
    textPassword_Id = (By.ID, "password")
    textConfirmPassword_NAME = (By.NAME, "password_confirmation")
    btnRegister_XPATH = (By.XPATH, "//button[normalize-space()='Register']")
    textStatus_XPATH = (By.XPATH, "//h2[normalize-space()='CredKart']")

    def __init__(self, driver):
        self.driver = driver

    def link_registration(self):
        self.driver.find_element(*UserRegistrationClass.linkRegistration_LinkText).click()

    def name(self, name):
        self.driver.find_element(*UserRegistrationClass.textName_NAME).send_keys(name)

    def email(self, email):
        self.driver.find_element(*UserRegistrationClass.textEmail_id).send_keys(email)

    def password(self, password):
        self.driver.find_element(*UserRegistrationClass.textPassword_Id).send_keys(password)

    def confirm_password(self, confirm_password):
        self.driver.find_element(*UserRegistrationClass.textConfirmPassword_NAME).send_keys(confirm_password)

    def btn_register(self):
        self.driver.find_element(*UserRegistrationClass.btnRegister_XPATH).click()

    def status(self):
        try:
            self.driver.find_element(*UserRegistrationClass.textStatus_XPATH)
            return True
        except NoSuchElementException:
            return False

    def generate_random_username(self):
        username = ''.join(random.choice(string.ascii_letters + string.digits) for _ in range(8))
        return username

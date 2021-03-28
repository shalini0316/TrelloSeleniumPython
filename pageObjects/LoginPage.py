from selenium.common.exceptions import TimeoutException
from selenium.webdriver.common.by import By
from selenium.common.exceptions import NoSuchElementException, TimeoutException, StaleElementReferenceException, \
    InvalidSelectorException, InvalidElementStateException
import base64
from selenium.webdriver.common.by import By
from selenium.webdriver import ActionChains
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.select import Select
from selenium.webdriver.support import ui
from utilities.BaseClass import BaseClass

class LoginPage(BaseClass):

    def __init__(self, driver):
        self.driver = driver

    loginButton = (By.XPATH, "//a[contains(text(),'Log')]")
    email = (By.ID, "user")
    password = (By.ID, "password")
    loginAtlassian = (By.ID, "login")
    submit = (By.ID, "login-submit")
    incorrectPassword = (By.XPATH, "//*[text()='Incorrect email address and / or password.']")
    profile = (By.XPATH, "(//*[@title='shalini (shalini474)']/span)[1]")
    logout = (By.XPATH, "//span[text()='Log out']")


    successMessage = (By.CSS_SELECTOR, "[class*='alert-success']")
    def getTitle(self):
        log = self.getLogger()
        try:
            return self.driver.title
        except TimeoutException as ex:
            log.info(ex)
        except StaleElementReferenceException as ex:
            log.info(ex)
        except InvalidElementStateException as ex:
            log.info(ex)
        except InvalidSelectorException as ex:
            log.info(ex)


    def clickLoginButton(self):
        log = self.getLogger()
        try:
            log.info("Login button is clicked")
            return self.driver.find_element(*LoginPage.loginButton).click()
        except TimeoutException as ex:
            log.info(ex)
        except StaleElementReferenceException as ex:
            log.info(ex)
        except InvalidElementStateException as ex:
            log.info(ex)
        except InvalidSelectorException as ex:
            log.info(ex)




    def enterEmail(self,email):
        log = self.getLogger()
        try:
            log.info("Email is entered:"+email)
            return self.driver.find_element(*LoginPage.email).send_keys(email)
        except TimeoutException as ex:
            log.info(ex)
        except StaleElementReferenceException as ex:
            log.info(ex)
        except InvalidElementStateException as ex:
            log.info(ex)
        except InvalidSelectorException as ex:
            log.info(ex)



    def enterPassword(self,password):
        log = self.getLogger()
        try:
            log.info("Password is entered: *******")
            self.driver.find_element(*LoginPage.password).clear()
            return self.driver.find_element(*LoginPage.password).send_keys(password)
        except TimeoutException as ex:
            log.info(ex)
        except StaleElementReferenceException as ex:
            log.info(ex)
        except InvalidElementStateException as ex:
            log.info(ex)
        except InvalidSelectorException as ex:
            log.info(ex)


    def clickSubmit(self):
        log = self.getLogger()
        try:
            log.info("Login button is clicked")
            return self.driver.find_element(*LoginPage.submit).click()
        except TimeoutException as ex:
            log.info(ex)
        except StaleElementReferenceException as ex:
            log.info(ex)
        except InvalidElementStateException as ex:
            log.info(ex)
        except InvalidSelectorException as ex:
            log.info(ex)


    def clickLoginAtlassian(self):
        log = self.getLogger()
        try:
            log.info("Login Atlassian button is clicked")
            return self.driver.find_element(*LoginPage.loginAtlassian).click()
        except TimeoutException as ex:
            log.info(ex)
        except StaleElementReferenceException as ex:
            log.info(ex)
        except InvalidElementStateException as ex:
            log.info(ex)
        except InvalidSelectorException as ex:
            log.info(ex)


    def getGender(self):
        log = self.getLogger()
        try:
            return self.driver.find_element(*LoginPage.gender)
        except TimeoutException as ex:
            log.info(ex)
        except StaleElementReferenceException as ex:
            log.info(ex)
        except InvalidElementStateException as ex:
            log.info(ex)
        except InvalidSelectorException as ex:
            log.info(ex)


    def submitForm(self):
        log = self.getLogger()
        try:
            return self.driver.find_element(*LoginPage.submit)
        except TimeoutException as ex:
            log.info(ex)
        except StaleElementReferenceException as ex:
            log.info(ex)
        except InvalidElementStateException as ex:
            log.info(ex)
        except InvalidSelectorException as ex:
            log.info(ex)


    def getSuccessMessage(self):
        log = self.getLogger()
        try:
         self.driver.find_element(*LoginPage.successMessage)


        except TimeoutException as ex:
            log.info(ex)
        except StaleElementReferenceException as ex:
            log.info(ex)
        except InvalidElementStateException as ex:
            log.info(ex)
        except InvalidSelectorException as ex:
            log.info(ex)


    def validateIncorrectPassword(self):
        log = self.getLogger()
        try:
             return self.driver.find_element(*LoginPage.incorrectPassword).is_displayed()


        except TimeoutException as ex:
            log.info(ex)
        except StaleElementReferenceException as ex:
            log.info(ex)
        except InvalidElementStateException as ex:
            log.info(ex)
        except InvalidSelectorException as ex:
            log.info(ex)



    def clickProfile(self):
        log = self.getLogger()
        try:
            log.info("Profile button is clicked")
            return self.driver.find_element(*LoginPage.profile).click()


        except TimeoutException as ex:
            log.info(ex)
        except StaleElementReferenceException as ex:
            log.info(ex)
        except InvalidElementStateException as ex:
            log.info(ex)
        except InvalidSelectorException as ex:
            log.info(ex)


    def clickLogout(self):
        log = self.getLogger()
        try:
            log.info("Logout is clicked")
            return self.driver.find_element(*LoginPage.logout).click()
        except TimeoutException as ex:
            log.info(ex)
        except StaleElementReferenceException as ex:
            log.info(ex)
        except InvalidElementStateException as ex:
            log.info(ex)
        except InvalidSelectorException as ex:
            log.info(ex)


from selenium.webdriver.common.by import By

import base64


class LoginPage:

    def __init__(self, driver):
        self.driver = driver

    loginButton = (By.LINK_TEXT, "Log in")
    email = (By.ID, "user")
    password = (By.ID, "password")
    loginAtlassian = (By.ID, "login")
    submit = (By.ID, "login-submit")
    incorrectPassword = (By.XPATH, "//*[text()='Incorrect email address and / or password.']")



    successMessage = (By.CSS_SELECTOR, "[class*='alert-success']")
    def getTitle(self):
       return self.driver.title

    def clickLoginButton(self):
       return self.driver.find_element(*LoginPage.loginButton).click()



    def enterEmail(self,email):
        return self.driver.find_element(*LoginPage.email).send_keys(email)


    def enterPassword(self,password):
        self.driver.find_element(*LoginPage.password).clear()
        return self.driver.find_element(*LoginPage.password).send_keys(password)

    def clickSubmit(self):
        return self.driver.find_element(*LoginPage.submit).click()

    def clickLoginAtlassian(self):
        return self.driver.find_element(*LoginPage.loginAtlassian).click()

    def getGender(self):
        return self.driver.find_element(*LoginPage.gender)

    def submitForm(self):
        return self.driver.find_element(*LoginPage.submit)

    def getSuccessMessage(self):
        return self.driver.find_element(*LoginPage.successMessage)

    def validateIncorrectPassword(self):
        return self.driver.find_element(*LoginPage.incorrectPassword).is_displayed()

    def decodePassword(self, password):
        print(base64.b64decode(password))

    def encodePassword(self, password):
        print(base64.b64encode(password))


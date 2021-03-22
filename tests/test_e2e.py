import pytest
from easygui import passwordbox
from selenium import webdriver
import time

from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

from pageObjects.DashboardPage import DashboardPage
from pageObjects.LoginPage import LoginPage
from utilities.BaseClass import BaseClass
from TestData.HomePageData import HomePageData


class TestOne(BaseClass):

    def test_e2e(self,getData):
        self.driver.get("https://trello.com/")
        self.driver.maximize_window()
        log = self.getLogger()
        log.info("........................................Test Case Started..............................................")
        #Login in to application
        loginPage = LoginPage(self.driver)
        loginPage.clickLoginButton()
         # Title is verified
        title=loginPage.getTitle()
        log.info("Title of the Application" + title)
        assert title == "Log in to Trello"
        self.isLabelExist("Continue with Google")
        self.isLabelExist("Continue with Microsoft")
        self.isLabelExist("Continue with Apple")
        loginPage.enterEmail(getData["Email"])
        log.info("Email is entered")
        loginPage.clickLoginAtlassian()
        time.sleep(3)
        #loginPage.enterPassword("test123")
        #loginPage.clickSubmit()
        #time.sleep(3)
        #loginPage.validateIncorrectPassword()
        #log.info("InCorrect Password is entered and validated")
        #time.sleep(3)
        password = passwordbox("PASSWORD:")
        time.sleep(3)
        loginPage.enterPassword(password)
        log.info("Correct Password is entered")
        loginPage.clickSubmit()
        time.sleep(3)
        log.info("Login button is clicked")
        time.sleep(3)



        #Create a new board
        dashboard = DashboardPage(self.driver)
        dashboard.page_has_loaded()
        dashboard.clickAddButton()
        log.info("Add button is clicked")
        time.sleep(3)
        dashboard.clickCreateBoard()
        log.info("Create Board button is clicked")
        time.sleep(3)
        dashboard.addBoardTitle(getData["BoardName"])
        log.info("Title for new board is entered")
        time.sleep(3)
        dashboard.clickCreateBoard()
        log.info("New Board is created")
        time.sleep(5)
        dashboard.page_has_loaded()



        #Create  Lists
        log.info("4 new lists are created")
        dashboard.enterListName(getData["List1"])
        time.sleep(5)
        dashboard.clickAddListBtn()
        time.sleep(3)
        dashboard.enterListName(getData["List2"])
        time.sleep(3)
        dashboard.clickAddListBtn()
        time.sleep(3)
        dashboard.enterListName(getData["List3"])
        time.sleep(3)
        dashboard.clickAddListBtn()
        time.sleep(3)
        dashboard.enterListName(getData["List4"])
        time.sleep(3)
        dashboard.clickAddListBtn()
        time.sleep(3)

        #Create 4 Cards
        log.info("4 cards are created")
        dashboard.clickAddCard()
        time.sleep(3)
        dashboard.enterCardName(getData["Card1"])
        dashboard.clickAddCardBtn()
        dashboard.enterCardName(getData["Card2"])
        dashboard.clickAddCardBtn()
        dashboard.enterCardName(getData["Card3"])
        dashboard.clickAddCardBtn()
        dashboard.enterCardName(getData["Card4"])
        dashboard.clickAddCardBtn()
        time.sleep(3)
        dashboard.clickCancelButton()
        time.sleep(3)
        dashboard.getCardNames()

        #Move card 2 to In Progress
        dashboard.rightClickCard(getData["Card2"])
        time.sleep(3)
        dashboard.clickMoveLabel()
        dashboard.selectListOptionByText(getData["List2"])
        time.sleep(3)
        dashboard.clickMoveButton()
        time.sleep(3)
        dashboard.card2MoveToInProgress()

        # Move card 3 to QA
        dashboard.rightClickCard(getData["Card3"])
        time.sleep(3)
        dashboard.clickMoveLabel()
        dashboard.selectListOptionByText(getData["List3"])
        time.sleep(3)
        dashboard.clickMoveButton()
        time.sleep(3)
        dashboard.card3MoveToQA()


         #Move card 2 to QA
        dashboard.rightClickCard(getData["Card2"])
        time.sleep(3)
        dashboard.clickMoveLabel()
        dashboard.selectListOptionByText(getData["List3"])
        time.sleep(3)
        dashboard.clickMoveButton()
        time.sleep(3)
        dashboard.card2MoveToQA()

        #Move card 1 to Current User
        time.sleep(3)
        dashboard.clickCard1()
        time.sleep(3)
        dashboard.clickMembers()
        time.sleep(3)
        dashboard.clickName()
        time.sleep(3)
        dashboard.enterComments(getData["Comments"])
        dashboard.clickSaveBtn()
        time.sleep(3)
        dashboard.clickCloseBtn()
        log.info( "........................................Test Case Completed..............................................")

        loginPage.clickProfile()
        loginPage.clickLogout()
        loginPage.clickLogout()

    @pytest.fixture(params=HomePageData.getTestData("Testcase1"))
    def getData(self, request):
        return request.param


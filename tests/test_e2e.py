import pytest
from selenium import webdriver
import time

from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

from pageObjects.DashboardPage import DashboardPage
from pageObjects.LoginPage import LoginPage
from utilities.BaseClass import BaseClass


class TestOne(BaseClass):

    def test_e2e(self):

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
        loginPage.enterEmail("shalini.jayakumar03@gmail.com")
        log.info("Email is entered")
        loginPage.clickLoginAtlassian()
        time.sleep(3)
        #loginPage.encodePassword("test1234")
        #loginPage.enterPassword("test123")
        #loginPage.clickSubmit()
        #time.sleep(3)
        #loginPage.validateIncorrectPassword()
        #log.info("InCorrect Password is entered and validated")
        #time.sleep(3)
        loginPage.enterPassword("test1234")
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
        dashboard.addBoardTitle("tst2")
        log.info("Title for new board is entered")
        time.sleep(3)
        dashboard.clickCreateBoard()
        log.info("New Board is created")
        time.sleep(5)
        dashboard.page_has_loaded()



        #Create  Lists
        log.info("4 new lists are created")
        dashboard.enterListName("Not Started")
        time.sleep(5)
        dashboard.clickAddListBtn()
        time.sleep(3)
        dashboard.enterListName("In Progress")
        time.sleep(3)
        dashboard.clickAddListBtn()
        time.sleep(3)
        dashboard.enterListName("QA")
        time.sleep(3)
        dashboard.clickAddListBtn()
        time.sleep(3)
        dashboard.enterListName("Done")
        time.sleep(3)
        dashboard.clickAddListBtn()
        time.sleep(3)

        #Create 4 Cards
        log.info("4 cards are created")
        dashboard.clickAddCard()
        time.sleep(3)
        dashboard.enterCardName("Card 1")
        dashboard.clickAddCardBtn()
        dashboard.enterCardName("Card 2")
        dashboard.clickAddCardBtn()
        dashboard.enterCardName("Card 3")
        dashboard.clickAddCardBtn()
        dashboard.enterCardName("Card 4")
        dashboard.clickAddCardBtn()
        time.sleep(3)
        dashboard.clickCancelButton()
        time.sleep(3)
        dashboard.getCardNames()

        #Move card 2 to In Progress
        dashboard.rightClickCard("Card 2")
        time.sleep(3)
        dashboard.clickMoveLabel()
        dashboard.selectListOptionByText("In Progress")
        time.sleep(3)
        dashboard.clickMoveButton()
        time.sleep(3)
        dashboard.card2MoveToInProgress()

        # Move card 3 to QA
        dashboard.rightClickCard("Card 3")
        time.sleep(3)
        dashboard.clickMoveLabel()
        dashboard.selectListOptionByText("QA")
        time.sleep(3)
        dashboard.clickMoveButton()
        time.sleep(3)
        dashboard.card3MoveToQA()


         #Move card 2 to QA
        dashboard.rightClickCard("Card 2")
        time.sleep(3)
        dashboard.clickMoveLabel()
        dashboard.selectListOptionByText("QA")
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
        dashboard.enterComments("I am done")
        dashboard.clickSaveBtn()
        time.sleep(3)
        dashboard.clickCloseBtn()
        log.info( "........................................Test Case Completed..............................................")




import pytest

from selenium import webdriver
import time

from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

from pageObjects.DashboardPage import DashboardPage
from pageObjects.LoginPage import LoginPage
from utilities.BaseClass import BaseClass
from utilities.Screenshot import SS
from TestData.HomePageData import HomePageData



class TestOne(BaseClass):

    def test_e2e(self,getData,getPassword):

        self.driver.get("https://trello.com/")
        time.sleep(3)
        self.driver.maximize_window()
        time.sleep(3)
        ss = SS(self.driver)
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
        loginPage.clickLoginAtlassian()
        time.sleep(3)
        loginPage.enterPassword(getPassword["password"])
        ss.ScreenShot("login.png")
        loginPage.clickSubmit()
        time.sleep(3)



        #Create a new board
        ss.ScreenShot("dashboard.png")
        dashboard = DashboardPage(self.driver)
        dashboard.page_has_loaded()
        dashboard.clickAddButton()
        time.sleep(3)
        ss.ScreenShot("addBoard.png")
        dashboard.clickCreateBoard()
        time.sleep(3)
        ss.ScreenShot("createBoard.png")
        dashboard.addBoardTitle(getData["BoardName"])
        time.sleep(3)
        dashboard.clickCreateBoard()
        time.sleep(5)
        dashboard.page_has_loaded()



        #Create  Lists
        log.info("4 new lists are created")
        dashboard.enterListName(getData["List1"])
        time.sleep(5)
        dashboard.clickAddListBtn()
        time.sleep(3)
        ss.ScreenShot("addList1.png")
        dashboard.enterListName(getData["List2"])
        time.sleep(3)
        dashboard.clickAddListBtn()
        time.sleep(3)
        ss.ScreenShot("addList2.png")
        dashboard.enterListName(getData["List3"])
        time.sleep(3)
        dashboard.clickAddListBtn()
        time.sleep(3)
        ss.ScreenShot("addList3.png")
        dashboard.enterListName(getData["List4"])
        time.sleep(3)
        dashboard.clickAddListBtn()
        time.sleep(3)
        dashboard.getListNames()
        ss.ScreenShot("addList4.png")

        #Create 4 Cards
        log.info("4 cards are created")
        dashboard.clickAddCard()
        time.sleep(3)
        dashboard.enterCardName(getData["Card1"])
        dashboard.clickAddCardBtn()
        ss.ScreenShot("cardName1.png")
        dashboard.enterCardName(getData["Card2"])
        dashboard.clickAddCardBtn()
        ss.ScreenShot("cardName2.png")
        dashboard.enterCardName(getData["Card3"])
        dashboard.clickAddCardBtn()
        ss.ScreenShot("cardName3.png")
        dashboard.enterCardName(getData["Card4"])
        dashboard.clickAddCardBtn()
        time.sleep(3)
        dashboard.clickCancelButton()
        time.sleep(3)
        ss.ScreenShot("cardName4.png")
        dashboard.getCardNames()

        #Move card 2 to In Progress
        dashboard.rightClickCard(getData["Card2"])
        time.sleep(3)
        dashboard.validateLabels()
        ss.ScreenShot("labels.png")
        time.sleep(3)
        dashboard.clickMoveLabel()
        dashboard.selectListOptionByText(getData["List2"])
        time.sleep(3)
        dashboard.clickMoveButton()
        time.sleep(3)
        dashboard.card2MoveToInProgress()
        ss.ScreenShot("card2Inprogress.png")

        # Move card 3 to QA
        dashboard.rightClickCard(getData["Card3"])
        time.sleep(3)
        dashboard.clickMoveLabel()
        dashboard.selectListOptionByText(getData["List3"])
        time.sleep(3)
        dashboard.clickMoveButton()
        time.sleep(3)
        dashboard.card3MoveToQA()
        ss.ScreenShot("card3QA.png")


         #Move card 2 to QA
        dashboard.rightClickCard(getData["Card2"])
        time.sleep(3)
        dashboard.clickMoveLabel()
        dashboard.selectListOptionByText(getData["List3"])
        time.sleep(3)
        dashboard.clickMoveButton()
        time.sleep(3)
        dashboard.card2MoveToQA()
        ss.ScreenShot("card2QA.png")

        #Move card 1 to Current User
        time.sleep(3)
        dashboard.clickCard1()
        time.sleep(3)
        dashboard.clickMembers()
        time.sleep(3)
        dashboard.clickName()
        time.sleep(3)
        ss.ScreenShot("name.png")
        dashboard.enterComments(getData["Comments"])
        dashboard.clickSaveBtn()
        ss.ScreenShot("comments.png")
        time.sleep(3)
        dashboard.clickCloseBtn()
        ss.ScreenShot("card1User.png")

        loginPage.clickProfile()
        loginPage.clickLogout()
        ss.ScreenShot("logout.png")
        loginPage.clickLogout()
        ss.writeDoc(getData["TestCase"])
        log.info(
            "........................................Test Case Completed..............................................")



    @pytest.fixture(params=HomePageData.getTestData())
    def getData(self, request):
        return request.param

    @pytest.fixture(params=HomePageData.getPassword())
    def getPassword(self, request):
        return request.param





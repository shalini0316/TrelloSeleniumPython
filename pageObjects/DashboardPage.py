from selenium.common.exceptions import NoSuchElementException, TimeoutException, StaleElementReferenceException, \
    InvalidSelectorException, InvalidElementStateException
from selenium.webdriver.common.by import By
from selenium.webdriver import ActionChains
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.select import Select
from selenium.webdriver.support import ui

from utilities.BaseClass import BaseClass


class DashboardPage(BaseClass):

    def __init__(self, driver):
        self.driver = driver



    addButton = (By.XPATH, "//button[@data-test-id='header-create-menu-button']")
    createboard = (By.XPATH, "//*[text()='Create board']")
    boardTitle = (By.XPATH, "//input[@data-test-id='create-board-title-input']")
    enterList = (By.XPATH, "//input[@placeholder='Enter list title…']")
    addList = (By.XPATH, "//*[text() = 'Add a list']")
    addListBtn = (By.XPATH, "//*[@value='Add list']")

    enterCard = (By.XPATH, "//textarea[@placeholder='Enter a title for this card…']")
    cardTitle = (By.XPATH, "(//span[text()='Add a card'])[1]")

    addCardBtn = (By.XPATH, "//input[@value='Add card']")
    addCard = (By.XPATH, "//*[text()='Add a card']")
    moveLabel = (By.XPATH, "//span[text()='Move']")

    moveBtn = (By.XPATH, "//input[@value='Move']")
    cancelBtn = (By.XPATH, "//a[@class='icon-lg icon-close dark-hover js-cancel']")
    closeBtn = (By.XPATH, "//a[@class='icon-md icon-close dialog-close-button js-close-window']")
    listDropdown = (By.XPATH, "//*[@class='js-select-list']")
    saveBtn = (By.XPATH, "//input[@type='submit' and @value='Save']")
    card1 = (By.XPATH, "//*[text() = 'Card 1']")
    members = (By.XPATH, "//span[text()='Members']")
    name = (By.XPATH, "//span[text()='shalini ']")
    comment = (By.XPATH, "//textarea[@placeholder='Write a comment…']")


    card3QA = (By.XPATH, "//span[text()='Card 3']/ancestor::div[@class='js-list list-wrapper']//h2[text()='QA']")
    card2QA = (By.XPATH, "//span[text()='Card 3']/ancestor::div[@class='js-list list-wrapper']//h2[text()='QA']")
    card2InProgress = (By.XPATH, "//span[text()='Card 2']/ancestor::div[@class='js-list list-wrapper']//h2[text()='In Progress']")
    cardNames= (By.XPATH, "//*[@class='list-card-title js-card-name']")
    def page_has_loaded(self):
        log = self.getLogger()
        try:
            page_state = self.driver.execute_script('return document.readyState;')
            return page_state == 'complete'

        except TimeoutException as ex:
            log.info(ex)
        except StaleElementReferenceException as ex:
            log.info(ex)
        except InvalidElementStateException as ex:
            log.info(ex)
        except InvalidSelectorException as ex:
            log.info(ex)

    def clickAddButton(self):
        log = self.getLogger()
        try:
            return self.driver.find_element(*DashboardPage.addButton).click()

        except NoSuchElementException as ex:
            log.info(ex)
        except TimeoutException as ex:
            log.info(ex)
        except StaleElementReferenceException as ex:
            log.info(ex)
        except InvalidElementStateException as ex:
            log.info(ex)
        except InvalidSelectorException as ex:
            log.info(ex)


    def clickCreateBoard(self):
        log = self.getLogger()
        try:
            return self.driver.find_element(*DashboardPage.createboard).click()

        except TimeoutException as ex:
            log.info(ex)
        except StaleElementReferenceException as ex:
            log.info(ex)
        except InvalidElementStateException as ex:
            log.info(ex)
        except InvalidSelectorException as ex:
            log.info(ex)
        return self.driver.find_element(*DashboardPage.createboard).click()

    def addBoardTitle(self,text):
        log = self.getLogger()
        try:
            return self.driver.find_element(*DashboardPage.boardTitle).send_keys(text)

        except TimeoutException as ex:
            log.info(ex)
        except StaleElementReferenceException as ex:
            log.info(ex)
        except InvalidElementStateException as ex:
            log.info(ex)
        except InvalidSelectorException as ex:
            log.info(ex)



    def clickAddListBtn(self):
        log = self.getLogger()
        try:
            return self.driver.find_element(*DashboardPage.addListBtn).click()

        except TimeoutException as ex:
            log.info(ex)
        except StaleElementReferenceException as ex:
            log.info(ex)
        except InvalidElementStateException as ex:
            log.info(ex)
        except InvalidSelectorException as ex:
            log.info(ex)


    def clickAddCardBtn(self):
        log = self.getLogger()
        try:
            return self.driver.find_element(*DashboardPage.addCardBtn).click()

        except TimeoutException as ex:
            log.info(ex)
        except StaleElementReferenceException as ex:
            log.info(ex)
        except InvalidElementStateException as ex:
            log.info(ex)
        except InvalidSelectorException as ex:
            log.info(ex)


    def clickAddCard(self):
        log = self.getLogger()
        try:
            return self.driver.find_element(*DashboardPage.addCard).click()

        except TimeoutException as ex:
            log.info(ex)
        except StaleElementReferenceException as ex:
            log.info(ex)
        except InvalidElementStateException as ex:
            log.info(ex)
        except InvalidSelectorException as ex:
            log.info(ex)


    def enterListName(self,text):
        log = self.getLogger()
        try:
            enterList = ui.WebDriverWait(self.driver, 10).until(
                EC.element_to_be_clickable((By.XPATH, "//input[@placeholder='Enter list title…']")))
            return enterList.send_keys(text)

        except TimeoutException as ex:
            log.info(ex)
        except StaleElementReferenceException as ex:
            log.info(ex)
        except InvalidElementStateException as ex:
            log.info(ex)
        except InvalidSelectorException as ex:
            log.info(ex)




    def clickAddList(self):
        log = self.getLogger()
        try:
            return self.driver.find_element(*DashboardPage.addList).click()

        except TimeoutException as ex:
            log.info(ex)
        except StaleElementReferenceException as ex:
            log.info(ex)
        except InvalidElementStateException as ex:
            log.info(ex)
        except InvalidSelectorException as ex:
            log.info(ex)


    def enterCardName(self,text):
        log = self.getLogger()
        try:
            return self.driver.find_element(*DashboardPage.enterCard).send_keys(text)

        except TimeoutException as ex:
            log.info(ex)
        except StaleElementReferenceException as ex:
            log.info(ex)
        except InvalidElementStateException as ex:
            log.info(ex)
        except InvalidSelectorException as ex:
            log.info(ex)


    def rightClickCard(self,label):
        log = self.getLogger()
        try:
            source = self.driver.find_element_by_xpath("//span[text()='"+label+"']")
            # action chain object
            action = ActionChains(self.driver)
            # right click operation
            return action.move_to_element(source).context_click(source).perform()

        except TimeoutException as ex:
            log.info(ex)
        except StaleElementReferenceException as ex:
            log.info(ex)
        except InvalidElementStateException as ex:
            log.info(ex)
        except InvalidSelectorException as ex:
            log.info(ex)


    def rightClickCard1(self):
        log = self.getLogger()
        try:
            source = self.driver.find_element_by_xpath("//span[text()='Card 1']")
            # action chain object
            action = ActionChains(self.driver)
            # right click operation
            return action.move_to_element(source).context_click(source).perform()

        except TimeoutException as ex:
            log.info(ex)
        except StaleElementReferenceException as ex:
            log.info(ex)
        except InvalidElementStateException as ex:
            log.info(ex)
        except InvalidSelectorException as ex:
            log.info(ex)

    def rightClickCard3(self):
        log = self.getLogger()
        try:
            source = self.driver.find_element_by_xpath("//span[text()='Card 3']")
            # action chain object
            action = ActionChains(self.driver)
            # right click operation
            return action.move_to_element(source).context_click(source).perform()

        except TimeoutException as ex:
            log.info(ex)
        except StaleElementReferenceException as ex:
            log.info(ex)
        except InvalidElementStateException as ex:
            log.info(ex)
        except InvalidSelectorException as ex:
            log.info(ex)

    def clickMoveButton(self):
        log = self.getLogger()
        try:
            return self.driver.find_element(*DashboardPage.moveBtn).click()

        except TimeoutException as ex:
            log.info(ex)
        except StaleElementReferenceException as ex:
            log.info(ex)
        except InvalidElementStateException as ex:
            log.info(ex)
        except InvalidSelectorException as ex:
            log.info(ex)

    def card2MoveToQA(self):
        log = self.getLogger()
        try:
            log.info("Card 2 is moved to QA")
            return self.driver.find_element(*DashboardPage.card2QA).is_displayed()

        except TimeoutException as ex:
            log.info(ex)
        except StaleElementReferenceException as ex:
            log.info(ex)
        except InvalidElementStateException as ex:
            log.info(ex)
        except InvalidSelectorException as ex:
            log.info(ex)

    def card3MoveToQA(self):
        log = self.getLogger()
        try:
            log.info("Card 3 is moved to QA")
            return self.driver.find_element(*DashboardPage.card3QA).is_displayed()

        except TimeoutException as ex:
            log.info(ex)
        except StaleElementReferenceException as ex:
            log.info(ex)
        except InvalidElementStateException as ex:
            log.info(ex)
        except InvalidSelectorException as ex:
            log.info(ex)

    def card2MoveToInProgress(self):
        log = self.getLogger()
        try:
            log.info("Card 2 is moved to In Progress")
            return self.driver.find_element(*DashboardPage.card2InProgress).is_displayed()

        except TimeoutException as ex:
            log.info(ex)
        except StaleElementReferenceException as ex:
            log.info(ex)
        except InvalidElementStateException as ex:
            log.info(ex)
        except InvalidSelectorException as ex:
            log.info(ex)


    def clickMoveLabel(self):
        log = self.getLogger()
        try:
            return self.driver.find_element(*DashboardPage.moveLabel).click()

        except TimeoutException as ex:
            log.info(ex)
        except StaleElementReferenceException as ex:
            log.info(ex)
        except InvalidElementStateException as ex:
            log.info(ex)
        except InvalidSelectorException as ex:
            log.info(ex)


    def clickCancelButton(self):
        log = self.getLogger()
        try:
            return self.driver.find_element(*DashboardPage.cancelBtn).click()

        except TimeoutException as ex:
            log.info(ex)
        except StaleElementReferenceException as ex:
            log.info(ex)
        except InvalidElementStateException as ex:
            log.info(ex)
        except InvalidSelectorException as ex:
            log.info(ex)


    def selectListOptionByText(self,text):
        log = self.getLogger()
        try:
            select = Select(self.driver.find_element_by_xpath("//*[@class='js-select-list']"))
            select.select_by_visible_text(text)


        except TimeoutException as ex:
            log.info(ex)
        except StaleElementReferenceException as ex:
            log.info(ex)
        except InvalidElementStateException as ex:
            log.info(ex)
        except InvalidSelectorException as ex:
            log.info(ex)



    def clickCard1(self):
        log = self.getLogger()
        try:
            return self.driver.find_element(*DashboardPage.card1).click()

        except TimeoutException as ex:
            log.info(ex)
        except StaleElementReferenceException as ex:
            log.info(ex)
        except InvalidElementStateException as ex:
            log.info(ex)
        except InvalidSelectorException as ex:
            log.info(ex)

    def clickMembers(self):
        log = self.getLogger()
        try:
            return self.driver.find_element(*DashboardPage.members).click()

        except TimeoutException as ex:
            log.info(ex)
        except StaleElementReferenceException as ex:
            log.info(ex)
        except InvalidElementStateException as ex:
            log.info(ex)
        except InvalidSelectorException as ex:
            log.info(ex)

    def clickName(self):
        log = self.getLogger()
        try:
            return self.driver.find_element(*DashboardPage.members).click()

        except TimeoutException as ex:
            log.info(ex)
        except StaleElementReferenceException as ex:
            log.info(ex)
        except InvalidElementStateException as ex:
            log.info(ex)
        except InvalidSelectorException as ex:
            log.info(ex)

    def enterComments(self, comment):
        log = self.getLogger()
        try:
            return self.driver.find_element(*DashboardPage.comment).send_keys(comment)

        except TimeoutException as ex:
            log.info(ex)
        except StaleElementReferenceException as ex:
            log.info(ex)
        except InvalidElementStateException as ex:
            log.info(ex)
        except InvalidSelectorException as ex:
            log.info(ex)

    def clickSaveBtn(self):
        log = self.getLogger()
        try:
            return self.driver.find_element(*DashboardPage.saveBtn).click()

        except TimeoutException as ex:
            log.info(ex)
        except StaleElementReferenceException as ex:
            log.info(ex)
        except InvalidElementStateException as ex:
            log.info(ex)
        except InvalidSelectorException as ex:
            log.info(ex)

    def clickCloseBtn(self):
        log = self.getLogger()
        try:
            return self.driver.find_element(*DashboardPage.closeBtn).click()

        except TimeoutException as ex:
            log.info(ex)
        except StaleElementReferenceException as ex:
            log.info(ex)
        except InvalidElementStateException as ex:
            log.info(ex)
        except InvalidSelectorException as ex:
            log.info(ex)


    def getCardNames(self):
        log = self.getLogger()
        try:
             for el in self.driver.find_elements(*DashboardPage.cardNames):
                 log.info("Card Name:"+el.text)

        except TimeoutException as ex:
            log.info(ex)
        except StaleElementReferenceException as ex:
            log.info(ex)
        except InvalidElementStateException as ex:
            log.info(ex)
        except InvalidSelectorException as ex:
            log.info(ex)
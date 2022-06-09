from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait
from selenium.common.exceptions import NoSuchElementException,\
                                       TimeoutException
from webdriver_manager.chrome import ChromeDriverManager


class BasePage():
    @classmethod
    def setHeadless(cls, params):
        pass

    @classmethod
    def setCookies(cls, params):
        pass

    def __init__(self) -> None:
        self.driver = webdriver.Chrome(service=Service(
                                       ChromeDriverManager().install()))

    def _visit(self, arg):
        pass

    def _getByType(self, locatorType):
        locatorType = locatorType.lower()
        if locatorType == 'id':
            return By.ID
        elif locatorType == 'name':
            return By.NAME
        elif locatorType == 'xpath':
            return By.XPATH
        elif locatorType == 'classname':
            return By.CLASS_NAME
        elif locatorType == 'linktext':
            return By.LINK_TEXT
        else:
            print(f'Locator "{locatorType}" is not supported')
        return False

    def isElementDisplayed(self, locatorType, locator, element=None,
                           to=15, pf=.45):
        by = self._getByType(locatorType)
        try:
            element = self.driver.find_element(by, locator)
        pass

    def _waitForElement(self, locator, to=10, pf=.5):
        try:
            wait = WebDriverWait(self.driver, timeout=to, poll_frequency=pf)
            element = wait.until(EC.visibility_of_element_located(
                                 (self._getByType('xpath'), locator)))
            return element
        except TimeoutException as TO:
            print(f'Element not found: {TO}')

    def _getElement(self, locator):
        pass

    def _getElements(self, locator):
        pass

    def _getText(self, locator):
        pass

    def _sendText(self, locator):
        pass

    def _clickElement(self, locator):
        pass

    def _webscroll(self, locator):
        pass

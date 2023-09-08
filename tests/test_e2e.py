import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

from pageObjects.CheckoutPage import CheckOutPage
from pageObjects.ConfirmPage import ConfirmPage
from pageObjects.HomePage import HomePage
from utilities.BaseClass import BaseClass


# @pytest.mark.usefixtures("setup")
"""
BaseClass has knowledge about setup fixture. TestOne inherit this parent class, 
automatically the child class TestOne also will have the knowledge of this fixture
So you need not explicitly define the fixture.
You will get that knowledge automatically as your parent have that.
"""
class TestOne(BaseClass):
    def test_e2e(self):
        log = self.getLogger()
        homePage = HomePage(self.driver)
        checkOutPage = homePage.shopItems()
        log.info("Getting all the items")

        products = checkOutPage.getCardTitles()
        for product in products:
            productName = product.find_element(By.CSS_SELECTOR, "div h4 a").text
            log.info(productName)
            if productName == "Blackberry":
                product.find_element(By.CSS_SELECTOR, "div button").click()
                break
        checkOutPage.checkOutBtnEl().click()

        checkOutPage.checkOutBtnSucEl().click()

        checkOutPage.countryItem().send_keys("Ch")
        log.info("Entering country name as Ch")
        # WebDriverWait(self.driver, 10).until(EC.presence_of_element_located((By.LINK_TEXT, "China")))
        self.verifyLinkPresence("China")
        self.driver.find_element(By.LINK_TEXT, "China").click()
        checkOutPage.agreeCheckBox().click()
        confirmPage = checkOutPage.submitItem()

        successText = confirmPage.sucItem().text
        log.info("Text received from application is " + successText)
        assert "Success" in successText












from selenium.webdriver.common.by import By

from pageObjects.ConfirmPage import ConfirmPage


class CheckOutPage:
    # driver.find_elements(By.CSS_SELECTOR, "div[class='card h-100']")
    cardTitle = (By.CSS_SELECTOR, "div[class='card h-100']")
    checkOutBtn = (By.CSS_SELECTOR, "a[class='nav-link btn btn-primary']")
    checkOutBtnSuc = (By.XPATH, "//button[@class='btn btn-success']")
    country = (By.CSS_SELECTOR, "#country")
    agree = (By.CSS_SELECTOR, "label[for='checkbox2']")
    purchase = (By.CSS_SELECTOR, "input[class='btn btn-success btn-lg']")
    def __init__(self, driver):
        self.driver = driver

    def getCardTitles(self):
        return self.driver.find_elements(*CheckOutPage.cardTitle)

    def checkOutBtnEl(self):
        return self.driver.find_element(*CheckOutPage.checkOutBtn)

    def checkOutBtnSucEl(self):
        return self.driver.find_element(*CheckOutPage.checkOutBtnSuc)

    def countryItem(self):
        return self.driver.find_element(*CheckOutPage.country)

    def agreeCheckBox(self):
        return self.driver.find_element(*CheckOutPage.agree)

    def submitItem(self):
        self.driver.find_element(*CheckOutPage.purchase).click()
        confirmPage = ConfirmPage(self.driver)
        return confirmPage
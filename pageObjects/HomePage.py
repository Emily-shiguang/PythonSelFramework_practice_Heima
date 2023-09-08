from selenium.webdriver.common.by import By

from pageObjects.CheckoutPage import CheckOutPage


class HomePage:
    def __init__(self, driver):
        self.driver = driver
    shop = (By.CSS_SELECTOR, "a[href*='shop']")

    name = (By.CSS_SELECTOR, "form div input[name='name']")
    email = (By.NAME, "email")
    chkbox = (By.ID, "exampleCheck1")
    gender = (By.ID, "exampleFormControlSelect1")
    submitbtn = (By.CSS_SELECTOR, "input[value='Submit']")
    successMessage = (By.CSS_SELECTOR, "[class*='alert-success']")

    def shopItems(self):
        self.driver.find_element(*HomePage.shop).click()
        checkOutPage = CheckOutPage(self.driver)
        return checkOutPage  # this way, you could skip create object in e2e, only create once in e2e

    def getName(self):
        return self.driver.find_element(*HomePage.name)

    def getEmail(self):
        return self.driver.find_element(*HomePage.email)

    def getCheckBox(self):
        return self.driver.find_element(*HomePage.chkbox)

    def getGender(self):
        return self.driver.find_element(*HomePage.gender)

    def submitForm(self):
        return self.driver.find_element(*HomePage.submitbtn)

    def getSuccessMessage(self):
        return self.driver.find_element(*HomePage.successMessage)
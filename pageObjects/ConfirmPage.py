from selenium.webdriver.common.by import By

class ConfirmPage:
    sucInfo = (By.CSS_SELECTOR, "[class='alert alert-success alert-dismissible']")
    def __init__(self, driver):
        self.driver = driver
    def sucItem(self):
        return self.driver.find_element(*ConfirmPage.sucInfo)
import pytest
from selenium.webdriver.common.by import By

from TestData.HomePageData import HomePageData
from pageObjects.HomePage import HomePage
from utilities.BaseClass import BaseClass


class TestHomePage(BaseClass):  # BaseClass: fixture will be available to this class
    def test_formSubmission(self, getData):
        log = self.getLogger()
        homePage = HomePage(self.driver)
        log.info("firstname is " + getData["firstname"])
        homePage.getName().send_keys(getData["firstname"])
        homePage.getEmail().send_keys(getData["lastname"])
        homePage.getCheckBox().click()
        self.selectOptionByText(homePage.getGender(), getData["gender"])
        homePage.submitForm().click()

        alertText = homePage.getSuccessMessage().text
        assert "success" in alertText
        self.driver.refresh()  # one way to refresh browser, else the send_keys input will append data during the second time

    # @pytest.fixture(params=HomePageData.test_HomePage_data)
    @pytest.fixture(params=HomePageData.getTestData("Testcase2"))
    def getData(self, request):
        return request.param


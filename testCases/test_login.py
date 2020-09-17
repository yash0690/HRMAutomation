import pytest
from selenium import webdriver


from PageObjects.LoginPage import LoginPage
from utilities.readProperties import ReadConfig
from utilities.customLogger import LogGen
#NamingConvention: Test_ID_nameoftestcase


class Test_001_Login():

    baseURL = ReadConfig.getApplicationURL()
    username = ReadConfig.getUseremail()
    password = ReadConfig.getpassword()
    logger = LogGen.loggen()

    def test_login(self, setup):

        self.logger.info("****Testcase_Login*****")
        self.driver = setup
        # Launching application
        self.driver.get(self.baseURL)
        # creating an object:
        self.lp = LoginPage(self.driver)
        self.logger.info("****Entering Username*****")
        self.lp.setUserName(self.username)
        self.logger.info("****Entering Password*****")
        self.lp.setPassword(self.password)
        self.logger.info("****Clicking on Login*****")
        self.lp.clickLogin()




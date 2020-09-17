#log into website with username and password and click on login
#on left hand side Menu - click on Admin > User management > users
#on right hand side click on +
#Enter all the new user details and click on SAVE
import time

from PageObjects.AdminMenuPage import AdminMenu
from PageObjects.LoginPage import LoginPage
from utilities.readProperties import ReadConfig
from utilities.customLogger import LogGen
#NamingConvention: Test_ID_nameoftestcase


class Test_002_Addnewuser():

    baseURL = ReadConfig.getApplicationURL()
    username = ReadConfig.getUseremail()
    password = ReadConfig.getpassword()
    logger = LogGen.loggen()

    def test_addnewuser(self, setup):
        self.logger.info("****Testcase_Login*****")
        self.driver = setup
        # Launching application
        self.driver.get(self.baseURL)
        # creating an object:
        self.lp = LoginPage(self.driver)
        self.lp.setUserName(self.username)
        self.lp.setPassword(self.password)
        self.lp.clickLogin()

        self.am = AdminMenu(self.driver)
        self.am.clickAdmin()
        self.am.clickUserManagement()
        self.am.clickUsers()
        time.sleep(5)



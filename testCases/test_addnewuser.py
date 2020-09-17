#log into website with username and password and click on login
#on left hand side Menu - click on Admin > User management > users
#on right hand side click on +
#Enter all the new user details and click on SAVE
import time

from selenium.webdriver.support.select import Select

from PageObjects.AddUserPage import AddUserPage
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
        time.sleep(10)

        #creating an object for AddUserPage

        self.au = AddUserPage(self.driver)
        self.au.clickAdd()
        time.sleep(5)
        self.au.setEmployeeName("Adella Lopez")
        time.sleep(5)
        self.au.setEmployeeUserName("hvhsjdb")
        #time.sleep(3)
        #dropdown = Select(self.au.setEssRoledropdown())
        #time.sleep(3)
        #dropdown.select_by_visible_text("Default ESS")  # by option what you are seeing on screen
        self.au.setEmployeePassword("ABCabc123$")
        self.au.setEmployeeConfirmPassword("ABCabc123$")
        self.au.clickSave()



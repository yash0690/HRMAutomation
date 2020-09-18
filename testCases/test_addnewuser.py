# log into website with username and password and click on login
# on left hand side Menu - click on Admin > User management > users
# on right hand side click on +
# Enter all the new user details and click on SAVE
import random
import string
import time

from selenium.webdriver.support.select import Select

from PageObjects.AddUserPage import AddUserPage
from PageObjects.AdminMenuPage import AdminMenu
from PageObjects.LoginPage import LoginPage
from utilities.readProperties import ReadConfig
from utilities.customLogger import LogGen


# NamingConvention: Test_ID_nameoftestcase


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

        # creating an object for AddUserPage

        self.au = AddUserPage(self.driver)
        self.au.clickAdd()
        time.sleep(5)
        self.au.setEmployeeName("Adella Lopez")
        time.sleep(5)
        randusername = random_generator()
        print(randusername)
        self.au.setEmployeeUserName(randusername)
        # time.sleep(3)
        # dropdown = Select(self.au.setEssRoledropdown())
        # time.sleep(3)
        # dropdown.select_by_visible_text("Default ESS")  # by option what you are seeing on screen
        self.au.setEmployeePassword("ABCabc123$")
        self.au.setEmployeeConfirmPassword("ABCabc123$")
        self.au.clickSave()
        time.sleep(5)
        self.au.clickfilter()
        time.sleep(2)
        self.au.setEmployeeusernamesearch(randusername)
        self.au.clicksearch()
        time.sleep(3)
        self.usernamexxx = self.driver.find_element_by_xpath("//tr[1]//td[2]/ng-include").text
        print(self.usernamexxx)

        if randusername == self.usernamexxx:
            assert True
            self.logger.info("********* Add New User Test Passed *********")
        else:
            self.driver.save_screenshot(".\\Screenshots\\" + "test_adduser_scr.png")  # Screenshot
            self.logger.error("********* Add New User Test Failed ************")
            assert False

        self.driver.close()
        self.logger.info("******* Ending Add New User test **********")


def random_generator(size=8, chars=string.ascii_lowercase):
    return ''.join(random.choice(chars) for x in range(size))

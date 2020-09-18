#Include all the page objects for Add User screen
class AddUserPage:

    button_add_xpath = "//i[contains(text(),'add')]"
    popup_form_id = "modal1"
    textbox_employeename_xpath = "//input[@id='selectedEmployee_value']"
    textbox_employeeusername_xpath = "//input[@id='user_name']"
    dropdown_essrole_id = "essrole"
    textbox_employeepassword_xpath = "//input[@id='password']"
    textbox_employeeconfirmpassword_xpath = "//input[@id='confirmpassword']"
    button_save_xpath = "//a[@id='systemUserSaveBtn']"
    button_filter_xpath = "//i[contains(text(),'ohrm_filter')]"
    textbox_employeeusernamesearch_xpath = "//input[@id='systemuser_uname_filter']"
    button_search_xpath = "//a[@class='modal-action modal-close waves-effect btn primary-btn']"




    def __init__(self, driver):
        self.driver = driver

    def clickAdd(self):
        self.driver.find_element_by_xpath(self.button_add_xpath).click()

    def addPopupForm(self):
        self.driver.find_element_by_id(self.popup_form_id)

    def setEmployeeName(self, employeename):
        self.driver.find_element_by_xpath(self.textbox_employeename_xpath).clear()
        self.driver.find_element_by_xpath(self.textbox_employeename_xpath).send_keys(employeename)

    def setEmployeeUserName(self, employeeusername):
        self.driver.find_element_by_xpath(self.textbox_employeeusername_xpath).clear()
        self.driver.find_element_by_xpath(self.textbox_employeeusername_xpath).send_keys(employeeusername)

    def setEssRoledropdown(self):
        self.driver.find_element_by_id(self.dropdown_essrole_id)


    def setEmployeePassword(self,password):
        self.driver.find_element_by_xpath(self.textbox_employeepassword_xpath).clear()
        self.driver.find_element_by_xpath(self.textbox_employeepassword_xpath).send_keys(password)


    def setEmployeeConfirmPassword(self,confirmpassword):
        self.driver.find_element_by_xpath(self.textbox_employeeconfirmpassword_xpath).clear()
        self.driver.find_element_by_xpath(self.textbox_employeeconfirmpassword_xpath).send_keys(confirmpassword)

    def clickSave(self):
        self.driver.find_element_by_xpath(self.button_save_xpath).click()

    def clickfilter(self):
        self.driver.find_element_by_xpath(self.button_filter_xpath).click()

    def setEmployeeusernamesearch(self,searchusername):
        self.driver.find_element_by_xpath(self.textbox_employeeusernamesearch_xpath).clear()
        self.driver.find_element_by_xpath(self.textbox_employeeusernamesearch_xpath).send_keys(searchusername)

    def clicksearch(self):
        self.driver.find_element_by_xpath(self.button_search_xpath).click()













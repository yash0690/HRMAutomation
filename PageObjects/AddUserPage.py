#Include all the page objects for Add User screen
class AddUserPage:
    
    button_add_xpath = "//i[contains(text(),'add')]"
    popup_form_id = "modal1"
    textbox_employeename_xpath = "//input[@id='selectedEmployee_value']"
    textbox_employeeusername_xpath = "//input[@id='user_name']"
    dropdown_essrole_xpath = "//input[@value='Default ESS']"
    dropdown_value_essrole_xpath = "//li[@class='active selected']//span[contains(text(),'Default ESS')]"
    textbox_employeepassword_xpath = "//input[@id='password']"
    textbox_employeeconfirmpassword_xpath = "//input[@id='confirmpassword']"
    button_save_xpath = "//a[@id='systemUserSaveBtn']"



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
        self.driver.find_element_by_xpath(self.dropdown_essrole_xpath).click()

    def setEssRoledrodpwnvalue(self):
        self.driver.find_element_by_xpath(self.dropdown_value_essrole_xpath).click()

    def setEmployeePassword(self,password):
        self.driver.find_element_by_xpath(self.textbox_employeepassword_xpath).clear()
        self.driver.find_element_by_xpath(self.textbox_employeepassword_xpath).send_keys(password)


    def setEmployeeConfirmPassword(self,confirmpassword):
        self.driver.find_element_by_xpath(self.textbox_employeeconfirmpassword_xpath).clear()
        self.driver.find_element_by_xpath(self.textbox_employeeconfirmpassword_xpath).send_keys(confirmpassword)

    def clickSave(self):
        self.driver.find_element_by_xpath(self.button_save_xpath).click()








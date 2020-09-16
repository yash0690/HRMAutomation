class LoginPage:
    textbox_username_xpath = "//input[@id='txtUsername']"
    textbox_password_xpath = "//input[@id='txtPassword']"
    button_login_xpath = "//input[@id='btnLogin']"

    def __init__(self, driver):
        self.driver = driver

    def setUserName(self,username):
        self.driver.find_element_by_xpath(self.textbox_username_xpath).clear()
        self.driver.find_element_by_xpath(self.textbox_username_xpath).send_keys(username)

    def setPassword(self,password):
        self.driver.find_element_by_xpath(self.textbox_password_xpath).clear()
        self.driver.find_element_by_xpath(self.textbox_password_xpath).send_keys(password)

    def clickLogin(self):
        self.driver.find_element_by_xpath(self.button_login_xpath).click()



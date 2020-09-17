#All page objects under Admin Menu on left hand side

class AdminMenu:

    def __init__(self,driver):
        self.driver = driver

    link_admin_xpath = "//span[contains(text(),'Admin')]"
    link_usermanagement_xpath = "//span[contains(text(),'User Management')]"
    link_users_xpath ="//span[@class='left-menu-title'][contains(text(),'Users')]"

    def clickAdmin(self):
        self.driver.find_element_by_xpath(self.link_admin_xpath).click()

    def clickUserManagement(self):
        self.driver.find_element_by_xpath(self.link_usermanagement_xpath).click()

    def clickUsers(self):
        self.driver.find_element_by_xpath(self.link_users_xpath).click()



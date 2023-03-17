from selenium.webdriver.chrome.webdriver import WebDriver
from selenium.webdriver.common.by import By


class Application:
    def __init__(self):
        self.wd = WebDriver()
        self.wd.implicitly_wait(60)

    def login(self, user_name, password):
        wd = self.wd
        wd.get("http://localhost/addressbook/")
        wd.find_element(By.NAME, "user").click()
        wd.find_element(By.NAME, "user").click()
        wd.find_element(By.NAME, "user").clear()
        wd.find_element(By.NAME, "user").send_keys(user_name)
        wd.find_element(By.NAME, "pass").click()
        wd.find_element(By.NAME, "pass").clear()
        wd.find_element(By.NAME, "pass").send_keys(password)
        wd.find_element(By.CSS_SELECTOR, "input[type=\"submit\"]").click()

    def logout(self):
        wd = self.wd
        wd.find_element(By.XPATH, "//a[text() = 'Logout']").click()

    def open_home_page(self):
        wd = self.wd
        wd.get("http://localhost/addressbook/")

    def open_groups_page(self):
        wd = self.wd
        wd.find_element(By.LINK_TEXT, "groups").click()

    def return_to_groups_page(self):
        wd = self.wd
        wd.find_element(By.XPATH, "//a[text() = 'group page']").click()

    def create_group(self, group):
        wd = self.wd
        wd.find_element(By.LINK_TEXT, "groups").click()
        # init group creation
        wd.find_element(By.NAME, "new").click()
        # fill group form
        wd.find_element(By.NAME, "group_name").click()
        wd.find_element(By.NAME, "group_name").clear()
        wd.find_element(By.NAME, "group_name").send_keys(group.name)
        wd.find_element(By.NAME, "group_header").click()
        wd.find_element(By.NAME, "group_header").clear()
        wd.find_element(By.NAME, "group_header").send_keys(group.header)
        wd.find_element(By.NAME, "group_footer").click()
        wd.find_element(By.NAME, "group_footer").clear()
        wd.find_element(By.NAME, "group_footer").send_keys(group.footer)
        # submit group creation
        wd.find_element(By.NAME, "submit").click()
        wd.find_element(By.XPATH, "//a[text() = 'group page']").click()

    def destroy(self):
        self.wd.quit()

from selenium.webdriver.common.by import By


class SessionHelper:
    def __init__(self, app):
        self.app = app

    def login(self, user_name="admin", password="secret"):
        wd = self.app.wd
        self.app.open_home_page()
        wd.find_element(By.NAME, "user").click()
        wd.find_element(By.NAME, "user").click()
        wd.find_element(By.NAME, "user").clear()
        wd.find_element(By.NAME, "user").send_keys(user_name)
        wd.find_element(By.NAME, "pass").click()
        wd.find_element(By.NAME, "pass").clear()
        wd.find_element(By.NAME, "pass").send_keys(password)
        wd.find_element(By.CSS_SELECTOR, "input[type=\"submit\"]").click()

    def logout(self):
        wd = self.app.wd
        wd.find_element(By.XPATH, "//a[text() = 'Logout']").click()

    def ensure_logout(self):
        wd = self.app.wd
        if self.is_logged_in():
            self.logout()

    def is_logged_in(self):
        wd = self.app.wd
        return len(wd.find_elements(By.XPATH, "//a[text() = 'Logout']")) > 0

    def is_logged_in_as(self, user_name):
        wd = self.app.wd
        return wd.find_element(By.XPATH, "//*[@name='logout']/b").text == "(" + user_name + ")"

    def ensure_login(self, user_name="admin", password="secret"):
        wd = self.app.wd
        if self.is_logged_in():
            if self.is_logged_in_as(user_name):
                return
            else:
                self.logout()
        self.login(user_name, password)
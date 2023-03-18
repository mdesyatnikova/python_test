from selenium.webdriver.common.by import By


class SessionHelper:
    def __init__(self, app):
        self.app = app

    def login(self, user_name, password):
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
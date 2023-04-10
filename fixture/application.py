from selenium import webdriver
from fixture.contact import ContactHelper
from fixture.group import GroupHelper
from fixture.session import SessionHelper


class Application:
    def __init__(self, browser, base_url):
        if browser == "chrome":
            self.wd = webdriver.Chrome()
        elif browser == "firefox":
            self.wd = webdriver.Firefox()
        else:
            raise ValueError(f"Unknown browser {browser}")
        self.session = SessionHelper(self)
        self.group = GroupHelper(self)
        self.contact = ContactHelper(self)
        self.base_url = base_url

    def is_valid(self):
        try:
            self.wd.current_url
            return True
        except:
            return False

    def open_home_page(self):
        self.wd.get(self.base_url)

    def destroy(self):
        self.wd.quit()

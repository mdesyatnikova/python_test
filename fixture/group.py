from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.webdriver import WebDriver

from model.group import Group


class GroupHelper:
    def __init__(self, app):
        self.app = app

    def open_groups_page(self):
        wd = self.app.wd
        if not (wd.current_url.endswith("/group.php") and len(wd.find_elements(By.NAME, "new")) > 0):
            wd.find_element(By.LINK_TEXT, "groups").click()

    def return_to_groups_page(self):
        wd = self.app.wd
        wd.find_element(By.XPATH, "//a[text() = 'group page']").click()

    def create(self, group):
        wd = self.app.wd
        self.open_groups_page()
        # init group creation
        wd.find_element(By.NAME, "new").click()
        # fill group form
        self.fill_group_form(group)
        # submit group creation
        wd.find_element(By.NAME, "submit").click()
        self.return_to_groups_page()

    def fill_group_form(self, group):
        wd = self.app.wd
        self.change_fild_value("group_name", group.name)
        self.change_fild_value("group_header", group.header)
        self.change_fild_value("group_footer", group.footer)

    def change_fild_value(self, fild_name, text):
        wd = self.app.wd
        if text is not None:
            wd.find_element(By.NAME, fild_name).click()
            wd.find_element(By.NAME, fild_name).clear()
            wd.find_element(By.NAME, fild_name).send_keys(text)

    def delete_first_group(self):
        self.delete_group_by_index(0)

    def delete_group_by_index(self, index):
        wd = self.app.wd
        self.open_groups_page()
        self.select_group(index)
        wd.find_element(By.NAME, "delete").click()
        self.return_to_groups_page()


    def select_first_group(self):
        wd = self.app.wd
        wd.find_element(By.NAME, "selected[]").click()

    def select_group(self, index):
        wd = self.app.wd
        wd.find_elements(By.NAME, "selected[]")[index].click()

    def edit_first_group(self, new_group_data):
        wd = self.app.wd
        self.open_groups_page()
        self.select_first_group()
        wd.find_element(By.NAME, "edit").click()
        self.fill_group_form(new_group_data)
        wd.find_element(By.NAME, "update").click()
        self.return_to_groups_page()

    def count(self):
        wd = self.app.wd
        self.open_groups_page()
        return len(wd.find_elements(By.NAME, "selected[]"))

    def get_group_list(self):
        wd = self.app.wd
        self.open_groups_page()
        group_list =[]
        for element in wd.find_elements(By.CSS_SELECTOR, "span.group"):
            text = element.text
            id_ = element.find_element(By.NAME, "selected[]").get_attribute("value")
            group_list.append(Group(name=text, id=id_))
        return group_list
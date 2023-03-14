from selenium.webdriver.chrome.webdriver import WebDriver
from selenium.webdriver.common.by import By
import unittest

def is_alert_present(wb):
    try:
        wb.switch_to_alert().text
        return True
    except:
        return False

class test_add_group(unittest.TestCase):
    def setUp(self):
        self.wd = WebDriver()
        self.wd.implicitly_wait(60)

    def test_add_group(self):
        success = True
        wd = self.wd
        wd.get("http://localhost/addressbook/")
        wd.find_element(By.NAME, "user").click()
        wd.find_element(By.NAME, "user").click()
        wd.find_element(By.NAME, "user").clear()
        wd.find_element(By.NAME, "user").send_keys("admin")
        wd.find_element(By.NAME, "pass").click()
        wd.find_element(By.NAME, "pass").clear()
        wd.find_element(By.NAME, "pass").send_keys("secret")
        wd.find_element(By.CSS_SELECTOR, "input[type=\"submit\"]").click()
        wd.find_element(By.LINK_TEXT, "groups").click()
        wd.find_element(By.NAME, "new").click()
        wd.find_element(By.NAME, "group_name").click()
        wd.find_element(By.NAME, "group_name").clear()
        wd.find_element(By.NAME, "group_name").send_keys("qwe")
        wd.find_element(By.NAME, "group_footer").click()
        wd.find_element(By.NAME, "group_footer").clear()
        wd.find_element(By.NAME, "group_footer").send_keys("qweqer")
        wd.find_element(By.NAME, "submit").click()
        wd.find_element(By.XPATH, "//a[text() = 'group page']").click()
        wd.find_element(By.XPATH, "//a[text() = 'Logout']").click()
        self.assertTrue(success)

    def tearDown(self):
        self.wd.quit()

if __name__ == "__main__":
    unittest.main()



from time import sleep
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC

from pages.base_page import Page

class ProjectPage(Page):
    NAME_FIELD = (By.ID, "Your-name")
    COMPANY_FIELD = (By.ID, "Your-company-name")
    PHONE_FIELD = (By.ID, "Phone")
    SEND_APP_BTN = (By.CSS_SELECTOR, "input[value='Send an application']")

    def verify_page(self):
        self.verify_partial_url("add-a-project")

    def add_test_info(self):
        self.find_element(*self.NAME_FIELD).clear()
        self.find_element(*self.NAME_FIELD).send_keys('test+davit+careearist')
        self.find_element(*self.PHONE_FIELD).clear()
        self.find_element(*self.PHONE_FIELD).send_keys('17327999106')
        self.find_element(*self.COMPANY_FIELD).clear()
        self.find_element(*self.COMPANY_FIELD).send_keys('test')

    def verify_test_info(self):
        assert self.find_element(*self.NAME_FIELD).get_attribute("value") == "test+davit+careearist"
        assert self.find_element(*self.COMPANY_FIELD).get_attribute("value") == "test"
        assert self.find_element(*self.PHONE_FIELD).get_attribute("value") == "17327999106"

    def verify_send_button(self):
        btn = self.wait.until(
            EC.element_to_be_clickable(self.SEND_APP_BTN)
        )







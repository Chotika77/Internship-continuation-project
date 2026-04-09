from time import sleep
from selenium.webdriver.common.by import By


from pages.base_page import Page

class EditPage(Page):
    NAME_FIELD = (By.ID, 'Fullname')
    PHONE_FIELD = (By.ID, 'number')
    COMPANY_FIELD = (By.ID, "Company-name")
    CLOSE_BUTTON = (By.CSS_SELECTOR, "a.close-button")
    SAVE_BUTTON = (By.XPATH, "//div[normalize-space()='Save changes']")

    def enter_test_information(self):
        self.find_element(*self.NAME_FIELD).clear()
        self.find_element(*self.NAME_FIELD).send_keys('test+davit+careearist')
        self.find_element(*self.PHONE_FIELD).clear()
        self.find_element(*self.PHONE_FIELD).send_keys('17327999106')
        self.find_element(*self.COMPANY_FIELD).clear()
        self.find_element(*self.COMPANY_FIELD).send_keys('test')

    def verify_profile_info(self, name, phone, company):
        actual_name = self.find_element(*self.NAME_FIELD).get_attribute('value')
        actual_phone = self.find_element(*self.PHONE_FIELD).get_attribute('value')
        actual_company = self.find_element(*self.COMPANY_FIELD).get_attribute('value')

        assert actual_name == name
        assert actual_phone == phone
        assert actual_company == company

    def verify_buttons(self):
        close_btn = self.find_element(*self.CLOSE_BUTTON)
        save_btn = self.find_element(*self.SAVE_BUTTON)

        assert close_btn.is_displayed(), "Close button not visible"
        assert save_btn.is_displayed(), "Save button not visible"

        assert close_btn.is_displayed(), "Close button not visible"
        assert save_btn.is_displayed(), "Save button not visible"












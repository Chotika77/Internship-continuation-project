from time import sleep
from selenium.webdriver.common.by import By

from pages.base_page import Page

class SettingsPage(Page):
    VERIFICATION_BUTTON = (By.XPATH, "//div[text()='Verification']")
    # MY_CLIENTS_BUTTON = (By.XPATH, "//div[text()='My clients']")
    EDIT_PROFILE_BUTTON = (By.CSS_SELECTOR, 'a[href="/profile-edit"]')
    MY_CLIENTS_OPTION = (By.XPATH, "//div[text()='My clients']")
    FOR_AGENCY_OPTION = (By.XPATH, "//div[text()='For agency']")
    ADD_PROJECT_OPTION = (By.XPATH, "//div[text()='Add a project']")


    def click_verification(self):
        self.click(*self.VERIFICATION_BUTTON)
        sleep(3)

    # def click_my_clients(self):
    #     self.click(*self.MY_CLIENTS_BUTTON)
    #     sleep(3)

    def click_edit_profile(self):
        self.click(*self.EDIT_PROFILE_BUTTON)

    def click_my_clients(self):
        self.click(*self.MY_CLIENTS_OPTION)

    def click_forag(self):
        self.click(*self.FOR_AGENCY_OPTION)
        sleep(3)

    def click_add_project(self):
        self.click(*self.ADD_PROJECT_OPTION)






from time import sleep
from selenium.webdriver.common.by import By

from pages.base_page import Page

class SettingsPage(Page):
    VERIFICATION_BUTTON = (By.XPATH, "//div[text()='Verification']")
    MY_CLIENTS_BUTTON = (By.XPATH, "//div[text()='My clients']")

    def click_verification(self):
        self.click(*self.VERIFICATION_BUTTON)
        sleep(3)

    def click_my_clients(self):
        self.click(*self.MY_CLIENTS_BUTTON)
        sleep(3)

from time import sleep
from selenium.webdriver.common.by import By

from pages.base_page import Page

class SettingsPage(Page):
    VERIFICATION_BUTTON = (By.XPATH, "//div[text()='Verification']")

    def click_verification(self):
        self.click(*self.VERIFICATION_BUTTON)
        sleep(3)
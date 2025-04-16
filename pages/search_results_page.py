from time import sleep
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select

from pages.base_page import Page

class SearchResultsPage(Page):
    SETTINGS_OPTIONS = (By.CSS_SELECTOR, "[class*='page-setting-block']")
    CONNECT_BUTTON = (By.XPATH, "//div[text()='Connect the company']")

    # def verify_page(self):
    #     self.verify_partial_url("settings")

    def verify_page(self):
        self.verify_partial_url("secondary-listings")

    def get_number_of_settings_options(self):
        options = self.find_elements(*self.SETTINGS_OPTIONS)
        return len(options)

    def verify_connect_button(self,expected_text):
        self.verify_text(expected_text, *self.CONNECT_BUTTON)

    # def verify_all_card_tags(self):









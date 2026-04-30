from time import sleep
from selenium.webdriver.common.by import By

from pages.base_page import Page

class ClientsPage(Page):
    DASHBOARD_BUTTON = (By.XPATH, "//a[text()='Dashboard']")

    def go_to_dashboard(self):
        self.click(*self.DASHBOARD_BUTTON)


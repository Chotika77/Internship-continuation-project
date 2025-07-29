from time import sleep
from selenium.webdriver.common.by import By

from pages.base_page import Page

class DashboardPage(Page):
    OFFERS_HEADER = (By.XPATH, "//div[@class='new-market-h1' and text()='Offers for you']")

    def wait_until_dashboard_loaded(self):
        self.wait_for_element_to_appear(*self.OFFERS_HEADER)


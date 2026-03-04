from time import sleep
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

from pages.base_page import Page

class DashboardPage(Page):
    # OFFERS_HEADER = (By.XPATH, "//div[@class='new-market-h1' and text()='Offers for you']")


    # OFF_PLAN_MENU = (By.XPATH, "(//*[normalize-space()='Off-plan'])[1]")

    # def wait_until_dashboard_loaded(self):
    #     # self.wait_for_element_to_appear(*self.OFFERS_HEADER)
    #     # print("g-menu-text count:",
    #     #       len(self.driver.find_elements(By.CSS_SELECTOR, "div.g-menu-text")))
    #     sleep(3)
    #     self.wait_for_element_to_appear(*self.OFF_PLAN_MENU)
    def wait_until_logged_in(self):
        WebDriverWait(self.driver, 15).until(
            EC.url_contains("find.reelly.io"))

from time import sleep
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select

from pages.base_page import Page

class MainPage(Page):
    FILTER_SELECTION = (By.ID, "Location-2")
    SETTINGS_OPTION = (By.XPATH, "//div[text()='Settings']")
    SECONDARY_OPTION = (By.XPATH, "//div[text()='Secondary']")
    def open_main(self):
        self.open('https://soft.reelly.io/')
        sleep(3)

    def select_presale(self):
      sleep(5)
      dd = self.find_element(*self.FILTER_SELECTION)
      select = Select(dd)
      select.select_by_value("Presale(EOI)")
      sleep(5)

    def click_settings(self):
        self.click(*self.SETTINGS_OPTION)
        sleep(3)

    def select_out_of_stock(self):
      sleep(5)
      dd = self.find_element(*self.FILTER_SELECTION)
      select = Select(dd)
      select.select_by_value("Out of stock")
      sleep(5)

    def click_secondary(self):
        self.click(*self.SECONDARY_OPTION)
        sleep(3)

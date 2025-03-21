from time import sleep
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select

from pages.base_page import Page

class MainPage(Page):
    FILTER_SELECTION = (By.ID, "Location-2")
    def open_main(self):
        self.open('https://soft.reelly.io/')
        sleep(3)

    def select_presale(self):
      sleep(5)
      dd = self.find_element(*self.FILTER_SELECTION)
      select = Select(dd)
      select.select_by_value("Presale(EOI)")
      sleep(5)
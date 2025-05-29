from time import sleep
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select

from pages.base_page import Page

class OffPlanPage(Page):
    NEXT_BUTTON_LOCATOR = (By.XPATH, "//div[text()='Next page']")
    PREVIOUS_BUTTON_LOCATOR = (By.XPATH,"//div[text()='Prev. page']")
    FILTER_SELECTION = (By.ID, "Location-2")


    # TOTAL_PAGE_NUMBER_LOCATOR = (By.XPATH, "//div[@class='pagination-text']/div[@wized='totalPageProperties']")
    # CURRENT_PAGE_NUMBER_LOCATOR = (By.XPATH, "//div[@class='pagination-text']/div[@wized='currentPageProperties']")


    def select_presale(self):
      sleep(5)
      dd = self.find_element(*self.FILTER_SELECTION)
      select = Select(dd)
      select.select_by_value("Presale(EOI)")
      sleep(5)

    def select_out_of_stock(self):
      sleep(5)
      dd = self.find_element(*self.FILTER_SELECTION)
      select = Select(dd)
      select.select_by_value("Out of stock")
      sleep(5)

    # def get_active_page_number(self):
    #     return int(self.find_element(*self.CURRENT_PAGE_NUMBER_LOCATOR).text)

    # def get_total_page_count(self):
    #     return int(self.find_element(*self.TOTAL_PAGE_NUMBER_LOCATOR).text)

    # def navigate_to_final_page(self):
    #     total_pages = self.get_total_page_count()
    #     current_page = self.get_active_page_number()
    #     while current_page < total_pages:
    #         self.navigate_to_next_page()
    #         sleep(3)
    #         current_page = self.get_active_page_number()
    #     print(f"Reached the final page ({total_pages}).")

    def navigate_to_final_page(self):
        total_pages = 1
        for page in range(total_pages + 1):
            self.wait_to_be_clickable_click(*self.NEXT_BUTTON_LOCATOR)

    def navigate_to_first_page(self):
        total_pages = 1
        for page in range(total_pages + 1):
            self.wait_to_be_clickable_click(*self.PREVIOUS_BUTTON_LOCATOR)


    def select_announced(self):
        sleep(5)
        dd = self.find_element(*self.FILTER_SELECTION)
        select = Select(dd)
        select.select_by_value("Announced")
        sleep(5)




    # def navigate_to_first_page(self):
    #     current_page = self.get_active_page_number()
    #     while current_page > 1:
    #         self.navigate_to_previous_page()
    #         sleep(3)
    #         current_page = self.get_active_page_number()
    #     print("Reached the first page.")
    #
    # def navigate_to_next_page(self):
    #     self.wait_to_be_clickable_click(*self.NEXT_BUTTON_LOCATOR)
    #
    # def navigate_to_previous_page(self):
    #     self.wait_to_be_clickable_click(*self.PREVIOUS_BUTTON_LOCATOR)

    # def _is_next_button_enabled(self):
    #     return True
    #
    # def _is_previous_button_enabled(self):
    #     return True







    # def navigate_to_next_page(self):
    #     if self._is_next_button_enabled():
    #         self.wait_to_be_clickable_click(*self.NEXT_BUTTON_LOCATOR)
    #
    # def navigate_to_previous_page(self):
    #     if self._is_previous_button_enabled():
    #         self.wait_to_be_clickable_click(*self.PREVIOUS_BUTTON_LOCATOR)
    #
    # def navigate_to_final_page(self):
    #     while self._is_next_button_enabled():
    #         self.navigate_to_next_page()
    #     print("Reached the final page.")
    #
    # def navigate_to_first_page(self):
    #     while self._is_previous_button_enabled():
    #         self.navigate_to_previous_page()
    #     print("Reached the first page.")
    #     # assert 'disabled' in self.find_element( * self.previous_button_locator).get_attribute(
    #     #     'class'), "Previous button is not disabled on the first page."
    #
    # def _is_next_button_enabled(self):
    #     next_button = self.find_element(*self.NEXT_BUTTON_LOCATOR)
    #     return 'disabled' not in next_button.get_attribute('class') and next_button.is_displayed()
    #
    # def _is_previous_button_enabled(self):
    #     previous_button = self.find_element(*self.PREVIOUS_BUTTON_LOCATOR)
    #     return 'disabled' not in previous_button.get_attribute('class') and previous_button.is_displayed()
    #

from time import sleep
from selenium.webdriver.common.by import By


from pages.base_page import Page

class SecondaryPage(Page):
    FILTER_BUTTON = (By.CSS_SELECTOR, ".filter-button")
    WANT_TO_BUY_BUTTON = (By. XPATH, "//div[text()='Want to buy']")
    # APPLY_FILTER = (By. XPATH, "//div[text()='Apply filter']")
    APPLY_FILTER = (By.CSS_SELECTOR, "a[class ='button-filter w-button']")



    def click_filter_button(self):
        self.click(*self.FILTER_BUTTON)

    def click_w_to_b(self):
        self.click(*self.WANT_TO_BUY_BUTTON)

    def click_apply_filter(self):
        self.click(*self.APPLY_FILTER)





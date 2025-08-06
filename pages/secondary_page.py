from time import sleep
from selenium.webdriver.common.by import By


from pages.base_page import Page

class SecondaryPage(Page):
    FILTER_BUTTON = (By.CSS_SELECTOR, ".filter-button")
    WANT_TO_BUY_BUTTON = (By. XPATH, "//div[text()='Want to buy']")
    # APPLY_FILTER = (By. XPATH, "//div[text()='Apply filter']")


    MIN_PRICE_INPUT = (By.XPATH, "//div[@class='select-text'][text()='from']/following-sibling::input[@type='text']")
    MAX_PRICE_INPUT = (By.XPATH,  "//div[@class='select-text'][text()='to']/following-sibling::input[@type='text']")
    APPLY_FILTER = (By.CSS_SELECTOR, "a[class ='button-filter w-button']")




    def click_filter_button(self):
        self.click(*self.FILTER_BUTTON)

    def click_w_to_b(self):
        self.click(*self.WANT_TO_BUY_BUTTON)

    def click_apply_filter(self):
        self.click(*self.APPLY_FILTER)

    # def set_min_price_filter(self, price):
    #     # self.input_text(self.MIN_PRICE_INPUT, price)
    #     sleep(3)
    #     element = self.find_element(*self.MIN_PRICE_INPUT)
    #     element.send_keys(price)


    # def set_max_price_filter(self, price):
    #     # self.input_text(self.MAX_PRICE_INPUT, price)
    #     element = self.find_element(*self.MAX_PRICE_INPUT)
    #     element.send_keys(price)

    def set_min_price_filter(self, price):
        self.wait_for_element_to_appear(*self.MIN_PRICE_INPUT)
        element = self.find_element(*self.MIN_PRICE_INPUT)
        element.clear()
        element.send_keys(price)

    def set_max_price_filter(self, price):
        self.wait_for_element_to_appear(*self.MAX_PRICE_INPUT)
        element = self.find_element(*self.MAX_PRICE_INPUT)
        element.clear()
        element.send_keys(price)



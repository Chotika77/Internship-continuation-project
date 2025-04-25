from time import sleep
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select

from pages.base_page import Page

class SearchResultsPage(Page):
    SETTINGS_OPTIONS = (By.CSS_SELECTOR, "[class*='page-setting-block']")
    CONNECT_BUTTON = (By.XPATH, "//div[text()='Connect the company']")
    PRODUCT_CARD_LOCATOR = (By.CSS_SELECTOR, "div[wized='listingCardMLS'].listing-card")
    PRICE_LOCATOR_IN_CARD = (By.CSS_SELECTOR, "div[wized='unitPriceMLS']")

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

    def get_all_product_cards(self):
        return self.find_elements(*self.PRODUCT_CARD_LOCATOR)

    def get_price_from_card(self, card_element):
        price_element = card_element.find_element(*self.PRICE_LOCATOR_IN_CARD)
        price_text = price_element.text.strip()
        cleaned_price = price_text.replace("AED ", "").replace(",", "")
        if cleaned_price.isdigit():
            return int(cleaned_price)
        return None

    def verify_price_within_range(self, min_price, max_price):
        cards = self.get_all_product_cards()
        lower_bound = int(min_price)
        upper_bound = int(max_price)
        all_prices_within_range = True
        for card in cards:
            price_value = self.get_price_from_card(card)
            if price_value is not None:
                if price_value < lower_bound or price_value > upper_bound:
                    price_element = card.find_element(*self.PRICE_LOCATOR_IN_CARD)
                    print(
                        f"Product price '{price_element.text.strip()}' ({price_value}) is outside the range {lower_bound} - {upper_bound}")
                    all_prices_within_range = False
                else:
                    print("Could not extract a valid price for a product card.")
                    all_prices_within_range = False
                    assert all_prices_within_range, f"Not all product prices are within the range {lower_bound} - {upper_bound}"











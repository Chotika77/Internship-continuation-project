from time import sleep
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

from pages.base_page import Page

class MainPage(Page):
    # FILTER_SELECTION = (By.ID, "Location-2")
    SETTINGS_OPTION = (By.XPATH, "//div[text()='Settings']")
    SECONDARY_OPTION = (By.XPATH, "//div[text()='Secondary']")
    # OFF_PLAN_OPTION = (By.XPATH, "//a[@href='/off-plan' and @class='menu-button-block w-inline-block']")
    # OFF_PLAN_OPTION = (By.XPATH, "//a[contains(@href, 'off-plan')]")
    # OFF_PLAN_OPTION =(By.XPATH, "//a[.//span[normalize-space()='Off-plan']]")
    OFF_PLAN_OPTION = (By.CSS_SELECTOR, '[wized="loadUser"] a[wized="newOffPlanLink"]')
    MARKET_OPTION = (By.XPATH, "//a[@href='/market-companies'][div[@class='g-menu-text' and text()='Market']]")
    VERIFICATION_OPTION = (By.XPATH, "//div[text()='Verification']")

    def open_main(self):
        self.open('https://soft.reelly.io/')
        sleep(3)

    # def select_presale(self):
    #   sleep(5)
    #   dd = self.find_element(*self.FILTER_SELECTION)
    #   select = Select(dd)
    #   select.select_by_value("Presale(EOI)")
    #   sleep(5)

    def click_settings(self):
        self.click(*self.SETTINGS_OPTION)
        sleep(3)

    # def select_out_of_stock(self):
    #   sleep(5)
    #   dd = self.find_element(*self.FILTER_SELECTION)
    #   select = Select(dd)
    #   select.select_by_value("Out of stock")
    #   sleep(5)

    def click_secondary(self):
        self.click(*self.SECONDARY_OPTION)
        sleep(3)

    def click_off_plan(self):
        print("DEBUG: Current URL:", self.driver.current_url)
        print("DEBUG: '/off-plan' in page:", "/off-plan" in self.driver.page_source)
        self.driver.maximize_window()
        # self.driver.refresh()
        sleep(5)
        # self.wait_for_element_to_appear(*self.OFF_PLAN_OPTION)
        # self.click(*self.OFF_PLAN_OPTION)
        # el = self.wait.until(
        #     EC.presence_of_element_located(self.OFF_PLAN_OPTION),
        #     message=f"Off-plan element {self.OFF_PLAN_OPTION} not found"
        # )
        # self.driver.execute_script("arguments[0].scrollIntoView({block: 'center'});", el)
        # self.driver.execute_script("arguments[0].scrollIntoView({block: 'center'});",
        #                            self.driver.find_element(*self.OFF_PLAN_OPTION))
        # WebDriverWait(self.driver, 10).until(
        #     EC.invisibility_of_element_located((By.XPATH, "//a[@wized='newOffPlanLink']"))
        # )
        self.wait_to_be_clickable_click(*self.OFF_PLAN_OPTION)




    def click_market(self):
        self.click(*self.MARKET_OPTION)
        sleep(3)

    def click_settings_option(self): #code duplication because of the behave step definition
        self.click(*self.SETTINGS_OPTION)
        sleep(3)


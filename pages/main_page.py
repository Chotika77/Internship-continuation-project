from time import sleep
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

from pages.base_page import Page

class MainPage(Page):
    # FILTER_SELECTION = (By.ID, "Location-2")
    # SETTINGS_OPTION = (By.XPATH, "//div[text()='Settings']")
    SETTINGS_OPTION = (By.CSS_SELECTOR, 'a[href="https://soft.reelly.io/settings"][class*="peer/menu-button"]')
    SIDEBAR_MENU = (By.CSS_SELECTOR, "div[wized='loadUser']")
    SECONDARY_OPTION = (By.XPATH, "//div[text()='Secondary']")
    # OFF_PLAN_OPTION = (By.XPATH, "//a[@href='/off-plan' and @class='menu-button-block w-inline-block']")
    # OFF_PLAN_OPTION = (By.XPATH, "//a[contains(@href, 'off-plan')]")
    # OFF_PLAN_OPTION =(By.XPATH, "//a[.//span[normalize-space()='Off-plan']]")
    OFF_PLAN_MENU = (By.XPATH, "//a[.//span[normalize-space()='Off-plan']]")
    MARKET_OPTION = (By.XPATH, "//a[@href='/' and contains(@class,'menu-button-block')]")
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
        # self.wait_to_be_clickable_click(*self.OFF_PLAN_MENU)
        el = self.driver.find_element(*self.OFF_PLAN_MENU)
        self.driver.execute_script("arguments[0].click();", el)




    def click_market(self):
        self.click(*self.MARKET_OPTION)
        sleep(3)

    def click_settings_option(self):
        # count = self.driver.execute_script(
        #     "return document.querySelectorAll('a[href=\"/settings\"]').length"
        # )
        # print("JS count:", count)
       # print("Page title:", self.driver.title)
       # print("Page source has menu-block:", "menu-block" in self.driver.page_source)

        # self.wait.until(lambda d: d.execute_script(
        #     "return document.querySelectorAll('a[href=\"/settings\"]').length > 0"
        # ))
        # self.wait_to_be_clickable_click(*self.SETTINGS_OPTION)

        sleep(10)
        self.wait_to_be_clickable(*self.SETTINGS_OPTION)
        self.wait_to_be_clickable_click(*self.SETTINGS_OPTION)
        sleep(3)

        # settings = self.wait.until(
        #     EC.presence_of_element_located(self.SETTINGS_OPTION)
        # )
        # self.driver.execute_script("arguments[0].scrollIntoView(true);", settings)
        # sleep(1)
        # settings.click()

        # settings = WebDriverWait(self.driver, 10).until(
        #     EC.presence_of_element_located(self.SETTINGS_OPTION)
        # )
        # print("Found:", settings.text)
        # settings.click()

        # settings = WebDriverWait(self.driver, 20).until(
        #     EC.presence_of_element_located((By.XPATH, "//a[@href='/settings']"))
        # )
        # settings.click()


            # sleep(5)
            # print("URL:", self.driver.current_url)
            # print("Found:", len(self.driver.find_elements(*self.SETTINGS_OPTION)))

            #


            # print("URL:", self.driver.current_url)
            # print("readyState:", self.driver.execute_script("return document.readyState"))
            # print("JS count:",
            #   self.driver.execute_script("return document.querySelectorAll('a[href=\"/settings\"]').length"))

    # def settings_exist(self,driver):
    #     return driver.execute_script(
    #         "return document.querySelectorAll('a[href=\"/settings\"]').length > 0"
    #     )
    #
    # def click_settings_option(self):
    #     self.wait.until(self.settings_exist)
    #     self.wait_to_be_clickable_click(*self.SETTINGS_OPTION)




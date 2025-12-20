from time import sleep
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select

from pages.base_page import Page

class MarketPage(Page):
    DEVELOPERS_FILTER = (By.XPATH, "//div[@fs-queryparam-name='markettagdeveloper'][div[@class='tag-text-proparties' and text()='Developers']]")
    AGENT_FILTER = (By.CSS_SELECTOR, ".new-market-tag.active")

    def click_developers(self):
        self.click(*self.DEVELOPERS_FILTER)
        sleep(3)


    def click_agent(self):
        self.click(*self.AGENT_FILTER)
        sleep(3)




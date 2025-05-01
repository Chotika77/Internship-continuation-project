from pages.base_page import Page
from pages.login_page import LoginPage
from pages.main_page import MainPage
from pages.search_results_page import SearchResultsPage
from pages.secondary_page import SecondaryPage
from pages.off_plan_page import OffPlanPage

class Application:
    def __init__(self, driver):
        self.page = Page(driver)
        self.main_page = MainPage(driver)
        self.login_page = LoginPage(driver)
        self.search_results_page = SearchResultsPage(driver)
        self.secondary_page = SecondaryPage(driver)
        self.off_plan_page = OffPlanPage(driver)
from pages.base_page import Page
from pages.login_page import LoginPage
from pages.main_page import MainPage
from pages.search_results_page import SearchResultsPage
from pages.secondary_page import SecondaryPage
from pages.off_plan_page import OffPlanPage
from pages.market_page import MarketPage
from pages.settings_page import SettingsPage
from pages.dashboard_page import DashboardPage
from pages.edit_page import EditPage
from pages.clients_page import ClientsPage
from pages.clients_dashboard_page import ClientsDashPage
from pages.agency_page import AgencyPage
from pages.project_page import ProjectPage


class Application:
    def __init__(self, driver):
        self.page = Page(driver)
        self.main_page = MainPage(driver)
        self.login_page = LoginPage(driver)
        self.search_results_page = SearchResultsPage(driver)
        self.secondary_page = SecondaryPage(driver)
        self.off_plan_page = OffPlanPage(driver)
        self.market_page = MarketPage(driver)
        self.settings_page = SettingsPage(driver)
        self.dashboard_page = DashboardPage(driver)
        self.edit_page = EditPage(driver)
        self.clients_page = ClientsPage(driver)
        self.clients_dashboard_page = ClientsDashPage(driver)
        self.agency_page = AgencyPage(driver)
        self.project_page = ProjectPage(driver)
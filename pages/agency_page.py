from time import sleep
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC

from pages.base_page import Page

class AgencyPage(Page):
    AGENCY_PAGE = (By.CSS_SELECTOR, ".agency-body")
    CONTACT_FORM = (By.ID, "wf-form-Corporate-Subscription-Pricing")

    def verify_page(self):
        self.wait_for_element_to_appear(*self.AGENCY_PAGE)

    def scroll_down(self):
        self.driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")

    def verify_contact_form(self):
        form = self.wait.until(
            EC.visibility_of_element_located(self.CONTACT_FORM)
        )

        assert form.is_displayed(), "Contact form is not visible"



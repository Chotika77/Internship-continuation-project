from time import sleep
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC

from pages.base_page import Page
class ClientsDashPage(Page):
    REFERRAL_INPUT = (By.ID, "invitation-2")

    def verify_referral_link(self):
        ref_input = self.wait.until(
            EC.visibility_of_element_located(self.REFERRAL_INPUT)
        )
        value = ref_input.get_attribute("value")

        assert "https://soft.reelly.io/sign-up" in value, (
            f"Referral link incorrect: {value}"
        )

    def verify_dashboard_page(self, url_part):
        self.verify_partial_url(url_part)
from selenium.webdriver.common.by import By
from time import sleep
from pages.base_page import Page
from selenium.webdriver.support.ui import WebDriverWait


class LoginPage(Page):
    EMAIL_FIELD = (By.CSS_SELECTOR, "[id='email-2']")
    PASSWORD_FIELD = (By.CSS_SELECTOR, "[id='field']")
    CONTINUE_BUTTON = (By.CSS_SELECTOR, "[wized='loginButton']")
    # PAGE_BODY = (By.CSS_SELECTOR, '.login-body')  # LOCATOR


    def log_in(self):
        sleep(2)
        self.wait_to_be_clickable(*self.EMAIL_FIELD)
        self.input_text('d.chkuaseli@yahoo.com', *self.EMAIL_FIELD)
        sleep(2)
        self.wait_to_be_clickable(*self.PASSWORD_FIELD)
        self.input_text('Sereli1977', *self.PASSWORD_FIELD)
        print("URL before click:", self.driver.current_url)
        self.wait_to_be_clickable_click(*self.CONTINUE_BUTTON)
        sleep(1)
        print("URL after click:", self.driver.current_url)
        # print("Still on sign-in:", "/sign-in" in self.driver.current_url)
        # print("Body contains error?:", "error" in self.driver.find_element(By.TAG_NAME, "body").text.lower())
        # print(self.driver.find_element(By.TAG_NAME, "body").text[:400])


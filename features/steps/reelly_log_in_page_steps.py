from behave import given, when, then
from time import sleep


@when('Log in to the page')
def log_in_to_the_page(context):
    context.app.login_page.log_in()
    # print("Current URL after clicking Continue:", context.driver.current_url)
    # print("Page title:", context.driver.title)
    # print("Windows:", len(context.driver.window_handles))
    # print("Has 'invalid' text:", "invalid" in context.driver.page_source.lower())
    # print("Has 'captcha' text:", "captcha" in context.driver.page_source.lower())
    # sleep(5)
    context.app.dashboard_page.wait_until_logged_in()
    # sleep(3)
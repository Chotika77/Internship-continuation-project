from behave import given, when, then
from time import sleep
from selenium.webdriver.common.by import By

@then('Verify that the right page is opened')
def verify_dashboard_page(context):
    context.app.clients_dashboard_page.verify_dashboard_page("referral/dashboard")

@then('Verify if the referral link contains "https://soft.reelly.io/sign-up"')
def verify_ref_link(context):
    context.app.clients_dashboard_page.verify_referral_link()

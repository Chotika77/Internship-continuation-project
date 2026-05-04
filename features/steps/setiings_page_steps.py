from behave import given, when, then
from time import sleep
from selenium.webdriver.common.by import By

@when('Click on the verification option')
def click_verification(context):
    context.app.settings_page.click_verification()

@when('Click on the “My clients” option')
def click_my_clients(context):
    context.app.settings_page.click_my_clients()


@when('Click on the Edit profile option')
def click_edit_profile(context):
    context.app.settings_page.click_edit_profile()

@when ('Click on "My Clients" profile option')
def click_my_clients(context):
    context.app.settings_page.click_my_clients()

@when ('Click "For agency" option')
def click_forag(context):
    context.app.settings_page.click_forag()




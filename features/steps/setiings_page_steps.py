from behave import given, when, then
from time import sleep
from selenium.webdriver.common.by import By

@when('Click on the verification option')
def click_verification(context):
    context.app.settings_page.click_verification()
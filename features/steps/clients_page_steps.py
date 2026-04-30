from behave import given, when, then
from time import sleep
from selenium.webdriver.common.by import By


@when('Go to "Dashboard" section')
def go_to_dashboard(context):
    context.app.clients_page.go_to_dashboard()



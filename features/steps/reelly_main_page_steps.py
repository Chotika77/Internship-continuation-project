from behave import given, when, then
from time import sleep


@given('open the main page')
def open_main(context):
    context.app.main_page.open_main()

@when('change the filter to presale')
def select_presale(context):
    context.app.main_page.select_presale()

@when('Click on settings option')
def click_settings(context):
    context.app.main_page.click_settings()
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

@when('change the filter to Out of Stock')
def select_out_of_stock(context):
    context.app.main_page.select_out_of_stock()

@when ('Click on “Secondary” option at the left side menu')
def click_secondary(context):
    context.app.main_page.click_secondary()

@when ('Click on off plan option at the left side menu')
def click_off_plan(context):
    context.app.main_page.click_off_plan()
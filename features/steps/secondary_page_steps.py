from behave import given, when, then
from time import sleep
from selenium.webdriver.common.by import By

@when ('Click on Filters')
def click_on_filters(context):
    context.app.secondary_page.click_filter_button()

@when ('Filter the products by “want to buy”')
def filter_by_w_to_b(context):
    context.app.secondary_page.click_w_to_b()

@when ('Click on Apply Filter')
def click_apply_filter(context):
    context.app.secondary_page.click_apply_filter()
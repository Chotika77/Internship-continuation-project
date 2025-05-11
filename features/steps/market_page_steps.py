from behave import given, when, then
from time import sleep


@when('Click on Developers filter at the top of the page')
def click_developers_filter(context):
    context.app.market_page.click_developers()

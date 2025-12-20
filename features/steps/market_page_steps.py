from behave import given, when, then
from time import sleep


@when('Click on Developers filter at the top of the page')
def click_developers_filter(context):
    context.app.market_page.click_developers()

@when('Click on “Agent” option in the upper right corner')
def click_agent_filter(context):
    context.app.market_page.click_agent()
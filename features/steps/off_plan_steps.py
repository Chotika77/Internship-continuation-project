from behave import given, when, then
from time import sleep
from selenium.webdriver.support.ui import Select
from pages.off_plan_page import OffPlanPage


@when('change the filter to presale')
def select_presale(context):
    context.app.main_page.select_presale()

@when('change the filter to Out of Stock')
def select_out_of_stock(context):
    context.app.main_page.select_out_of_stock()

@when ('Go to the final page using the pagination button')
def step_impl(context):
    context.off_plan_page = OffPlanPage(context.driver)
    # while context.off_plan_page._is_next_button_enabled():
    #     context.off_plan_page.navigate_to_next_page()
    # print("Reached the final page.")
    context.off_plan_page.navigate_to_final_page()

@when('Go back to the first page using the pagination button')
def step_impl(context):
    # while context.off_plan_page._is_previous_button_enabled():
    #     context.off_plan_page.navigate_to_previous_page()
    # print("Reached the first page.")
    context.off_plan_page.navigate_to_first_page()

@when ('Filter by sale status of “Announced”')
def step_impl(context):
    context.app.off_plan_page.select_announced()

@when ('Filter off-plan products by price range from {min_price} to {max_price} AED')
def step_off_plan_price_filter(context, min_price, max_price):
    context.app.off_plan_page.click_apply_filter_bn()
    context.app.off_plan_page.set_min_price_filter(min_price)
    context.app.off_plan_page.set_max_price_filter(max_price)
    context.app.off_plan_page.click_show_projects()




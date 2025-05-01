from behave import given, when, then
from time import sleep
from pages.off_plan_page import OffPlanPage

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
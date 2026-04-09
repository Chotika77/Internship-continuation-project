from behave import given, when, then
from time import sleep
from selenium.webdriver.common.by import By

@when ('Enter some test information in the input fields')
def enter_test_information(context):
    context.app.edit_page.enter_test_information()

@then('Check the right information is present in the input fields')
def verify_information(context):
    context.app.edit_page.verify_profile_info(
        "test+davit+careearist",
        "17327999106",
        "test"
    )


@then('Check the “Close” and “Save Changes” buttons are available and clickable')
def verify_buttons(context):
    context.app.edit_page.verify_buttons()



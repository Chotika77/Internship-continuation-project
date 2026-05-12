from behave import given, when, then

@then('Verify that project page is opened')
def verify_page(context):
    context.app.project_page.verify_page()

@when("Add some test information to the input fields")
def add_test_info(context):
    context.app.project_page.add_test_info()

@then("Verify the right information is present in the input fields")
def verify_test_info(context):
    context.app.project_page.verify_test_info()

@then('Verify the “Send an application” button is available and clickable')
def verify_send_button(context):
    context.app.project_page.verify_send_button()

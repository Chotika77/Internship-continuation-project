from behave import given, when, then

@then('Verify agency page opens')
def verify_page(context):
    context.app.agency_page.verify_page()


@when('Scroll down to the bottom of the page')
def scroll_down(context):
    context.app.agency_page.scroll_down()


@then ('Verify that the "Contact us for details" form is available')
def verify_contact_form(context):
    context.app.agency_page.verify_contact_form()





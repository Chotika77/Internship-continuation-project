from behave import given, when, then
from time import sleep
from selenium.webdriver.common.by import By

LISTINGS = (By.CSS_SELECTOR, "a[wized='cardOfProperty']")
SALES_STATUS = (By.CSS_SELECTOR, "div[wized='projectStatus']")



@then('Verify each product contains the Presale')
def verify_filter_status(context):
    context.driver.execute_script("window.scrollBy(0,2000)", "")
    sleep(4)
    context.driver.execute_script("window.scrollBy(0,2000)", "")



    all_products = context.driver.find_elements(*LISTINGS)
    # print(all_products)


    for product in all_products:
        status_tag = product.find_element(*SALES_STATUS).text
        assert status_tag == "Presale(EOI)", f'Expected "Presale(EOI)" but got {status_tag.text}'


@then('Verify the right page opens')
def verify_right_page_opens(context):
    context.app.search_results_page.verify_partial_url("settings")


@then('Verify there are 13 options for the settings')
def verify_settings_option_count(context):
    actual_option_count = context.app.search_results_page.get_number_of_settings_options()
    expected_option_count = 13
    assert actual_option_count == expected_option_count, \
        f"Expected {expected_option_count} settings options, but found {actual_option_count}"
    print(f"Successfully verified that there are {expected_option_count} settings options.")


@then ('Verify “Connect the company” button is available')
def verify_connect_button(context):
    context.app.search_results_page.verify_connect_button('Connect the company')


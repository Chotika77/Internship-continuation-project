from behave import given, when, then
from time import sleep
from selenium.webdriver.common.by import By

LISTINGS = (By.CSS_SELECTOR, "a[wized='cardOfProperty']")
SALES_STATUS = (By.CSS_SELECTOR, "div[wized='projectStatus']")
SECONDARY_LISTINGS = (By.CSS_SELECTOR,"[wized*='listingCard']")
SALES_TAG = (By.XPATH, "//div[text()= 'Want to buy']")





@then('Verify each product contains {expected_status}')
def verify_filter_status(context, expected_status):
    context.driver.execute_script("window.scrollBy(0,2000)", "")
    sleep(4)
    context.driver.execute_script("window.scrollBy(0,2000)", "")



    all_products = context.driver.find_elements(*LISTINGS)
    # print(all_products)


    for product in all_products:
        status_text = product.find_element(*SALES_STATUS).text.strip()
        assert status_text == expected_status, f'Expected {expected_status} but got {status_text}'


# @then('Verify the right page opens')
# def verify_right_page_opens(context):
#     context.app.search_results_page.verify_partial_url("settings")

@then('Verify the right page opens')
def verify_right_page_opens(context):
    context.app.search_results_page.verify_partial_url("secondary-listings")


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

@then ('Verify all cards have “Want to buy” tag')
def verify_all_card_tags(context):
    context.driver.execute_script("window.scrollBy(0,2000)", "")
    sleep(4)
    context.driver.execute_script("window.scrollBy(0,2000)", "")

    all_sec_products = context.driver.find_elements(*SECONDARY_LISTINGS)

    for product in all_sec_products:
        status_tag_text = product.find_elements(*SALES_TAG)[0].text.strip()
        assert status_tag_text == "Want to buy", f'Expected "Want to buy"  but got {status_tag_text}'


@then('Verify the price in all cards is inside the range {min_price} - {max_price}')
def step_impl(context, min_price, max_price):
    context.app.search_results_page.verify_price_within_range(min_price, max_price)



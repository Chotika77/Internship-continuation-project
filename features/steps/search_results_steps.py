from behave import given, when, then
from time import sleep
from selenium.webdriver.common.by import By


LISTINGS = (By.CSS_SELECTOR, "a[wized='cardOfProperty']")
SALES_STATUS = (By.CSS_SELECTOR, "div[wized='projectStatus']")
SECONDARY_LISTINGS = (By.CSS_SELECTOR,"[wized*='listingCard']")
SALES_TAG = (By.XPATH, "//div[text()= 'Want to buy']")
MARKET_LISTINGS = (By.CSS_SELECTOR, "a[wized='marketPageCard']")
LICENSE_TAG = (By.CSS_SELECTOR, "div.license-block")
UPLOAD_IMAGE_BUTTON = (By.XPATH, "//label[@class='upload-button-2' and @for='input_file']")
NEXT_STEP_BUTTON = (By.XPATH, "//div[contains(text(), 'Next step')]")
PRODUCT_TITLES = (By.CSS_SELECTOR, "div[wized='projectName']")
PRODUCT_IMAGES = (By.CSS_SELECTOR, "div[wized='projectImage']")
OFFERS_LISTINGS = (By.CSS_SELECTOR, ".new-market-cards .new-market-card")
OFFERS_TAGS = (By.XPATH, "//div[@wized='servicesOffersCardCientTagText']")










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
#
# @then('Verify the right page opens')
# def verify_right_page_opens(context):
#     context.app.search_results_page.verify_partial_url("secondary-listings")

# @then('Verify the right page opens')
# def verify_right_page_opens(context):
#     context.app.search_results_page.verify_off_plan_page()

# @then('Verify the right page opens')
# def verify_right_page_opens(context):
#     context.app.search_results_page.verify_market_page()

@then('Verify the right page opens')
def verify_right_page_opens(context):
    context.app.search_results_page.verify_my_clients_page()

# @then('Verify the right page opens')
# def verify_right_page_opens(context):
#     context.app.search_results_page.verify_partial_url("verification")

@then ('Verify “upload image” and “Next step” buttons are available')
def verify_buttons(context):
    upload_image_button = context.driver.find_element(*UPLOAD_IMAGE_BUTTON)
    next_step_button = context.driver.find_element(*NEXT_STEP_BUTTON)

    assert upload_image_button.is_displayed() == True, f'"Upload image" button expected to be visible but was not.'
    assert next_step_button.is_displayed() == True, f'"Next step" button expected to be visible but was not.'






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

@then('Verify all cards has the license tag')
def verify_tag(context):
    context.driver.execute_script("window.scrollBy(0,2000)", "")
    sleep(4)
    context.driver.execute_script("window.scrollBy(0,2000)", "")

    all_market_products = context.driver.find_elements(*MARKET_LISTINGS)

    for product in all_market_products:
        license_tag_text = product.find_elements(*LICENSE_TAG)[0].text.strip()
        assert license_tag_text == "License", f'Expected "License"  but got {license_tag_text}'


@then('Verify each product on this page contains a title and picture visible')
def verify_product_titles_and_pictures(context):
    context.driver.execute_script("window.scrollBy(0, 2000)", "")
    sleep(4)
    context.driver.execute_script("window.scrollBy(0, 2000)", "")


    titles = context.driver.find_elements(*PRODUCT_TITLES)
    for title in titles:
        assert title.is_displayed() == True, f'A product title was expected to be visible but was not.'

    images = context.driver.find_elements(*PRODUCT_IMAGES)
    for image in images:
        assert image.is_displayed() == True, f'A product image was expected to be visible but was not.'

@then('Verify the price in all off-plan cards is inside the range {min_price} - {max_price}')
def step_impl(context, min_price, max_price):
        context.app.search_results_page.verify_off_plan_price_within_range(min_price, max_price)



@then('Verify all the offers shown have "Agent" tag')
def verify_agent_tag(context):
    context.driver.execute_script("window.scrollBy(0,2000)", "")
    sleep(4)
    context.driver.execute_script("window.scrollBy(0,2000)", "")

    all_offers_cards = context.driver.find_elements(*OFFERS_LISTINGS)
    for offer in all_offers_cards:
        status_tag_text = offer.find_elements(*OFFERS_TAGS)[0].text.strip()
        assert status_tag_text == "Agent", f'Expected "Agent" but got {status_tag_text}'


@then('Verify that the page contains the 7 options')
def verify_option_count(context):
    actual_count = context.app.search_results_page.get_number_of_options()
    expected_count = 7
    assert actual_count == expected_count, \
        f"Expected {expected_count} options, but found {actual_count}"











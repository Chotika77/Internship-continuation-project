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
        status = product.find_element(*SALES_STATUS).text
        assert status != '', 'Product title not shown'
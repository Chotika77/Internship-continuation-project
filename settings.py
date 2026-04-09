# from selenium import webdriver
# from selenium.webdriver.common.by import By
# from selenium.webdriver.chrome.service import Service
# from webdriver_manager.chrome import ChromeDriverManager
# from time import sleep
#
# driver_path = ChromeDriverManager().install()
# service = Service(driver_path)
# driver = webdriver.Chrome(service=service)
# driver.maximize_window()
#
# driver.get('https://soft.reelly.io')
#
# sleep(15)
#
# EMAIL_FIELD = (By.CSS_SELECTOR, "[id='email-2']")
# PASSWORD_FIELD = (By.CSS_SELECTOR, "[id='field']")
# CONTINUE_BUTTON = (By.CSS_SELECTOR, "[wized='loginButton']")
# #login
# driver.find_element(*EMAIL_FIELD).send_keys('d.chkuaseli@yahoo.com')
# driver.find_element(*PASSWORD_FIELD).send_keys('Sereli1977')
# driver.find_element(*CONTINUE_BUTTON).click()
#
# sleep(15)
#
# driver.find_element(By.CSS_SELECTOR, 'a[href="https://soft.reelly.io/settings"][class*="peer/menu-button"]').click()
# sleep(5)
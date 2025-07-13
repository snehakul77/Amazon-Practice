#Automate login functionality using selenium
import selenium
import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import logging

logging.basicConfig(
    filename='test_logins.log',
    level = logging.INFO,
    format = '%(asctime)s - %(levelname)s - %(message)s'
)

driver = webdriver.Chrome()

driver.get("https://www.amazon.de/ap/signin?openid.pape.max_auth_age=0&openid.return_to=https%3A%2F%2Fwww.amazon.de%2F%3Fref_%3Dnav_signin&openid.identity=http%3A%2F%2Fspecs.openid.net%2Fauth%2F2.0%2Fidentifier_select&openid.assoc_handle=deflex&openid.mode=checkid_setup&openid.claimed_id=http%3A%2F%2Fspecs.openid.net%2Fauth%2F2.0%2Fidentifier_select&openid.ns=http%3A%2F%2Fspecs.openid.net%2Fauth%2F2.0")
driver.maximize_window()

driver.find_element(By.ID,"ap_email").send_keys("snehakrishna.kulkarni@outlook.com")
driver.find_element(By.ID,"continue").click()
driver.find_element(By.NAME,"password").send_keys("Ganapati_pune15$")
driver.find_element(By.ID,"auth-signin-button").click()

time.sleep(5)

if "signin" in driver.current_url:
    logging.info("Page login was successful")
    print("Login Successful")
else:
    print("Login Failed")
    logging.info("Login Failed")

driver.quit()

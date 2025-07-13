#Selenium with webdriver wait

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.keys import Keys

driver = webdriver.Chrome()
driver.get("https://www.amazon.in")
driver.maximize_window()

wait = WebDriverWait(driver,10)

wait.until(EC.presence_of_element_located((By.ID,"username"))).send_keys("snehakrishna.kulkarni@outlook.com")
driver.find_element_by_id("password").send_keys("<PASSWORD>")
driver.find_element_by_id("loginbutton").click()

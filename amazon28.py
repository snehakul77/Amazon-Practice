#API and UI validation for a product details page.
from re import match

import pytest
import requests
from selenium import webdriver
from selenium.webdriver.common.by import By

@pytest.fixture
def driver():
    driver = webdriver.Chrome()
    driver.maximize_window()
    yield driver
    driver.quit()

def test_api_ui_sync(driver):
    product_id = "B08N5WRWNW"
    url = f"https://api.example.com/products/{product_id}"
    response = requests.get(url)
    assert response.status_code == 200
    product= response.json()
    api_title = product["title"]

    #UI to validate with above api respone

    driver.get(f"https://www.amazon.com/dp/{product_id}")
    ui_title = driver.find_element(By.ID,  "UI Title").text
    assert ui_title == api_title   $ , "API title and UI title do not match"
#Test flakiness in selenium code can be resolved by adding explicit waits.

from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

def test_add_to_cart(driver):
    driver.get("url")

    wait = WebDriverWait(driver,10)
    add_btn = wait.until(EC.presence_of_element_located(By.ID,"add-to-cart"))
    add_btn.click()

    assert "cart" in driver.current_url

    
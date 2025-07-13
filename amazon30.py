# Automation framework design for amazon cart page, where can verify number of items,
# delete items, update quantity and verify price.

#Step 1: Create a basepage file where i will  add all the reusable code like launching websites/logins

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.keys import Keys

#This is a different file where we create a basepage.py file with all common modules
class BasePage:
    def __init__(self, driver):
        self.driver = driver

    def click(self,locator,by):
        self.driver.find_element(by, locator).click()

    def type_text(self,locator,by,text):
        field = self.driver.find_element(by, locator)
        field.clear()
        field.send_keys(text)


#Step 2 we will create a cart page with locators and the actions to be performed.

class cartPage(BasePage):
    CART_Item = (By.CSS_SELECTOR, "#cart")
    Delete_Button = (By.CSS_SELECTOR, "#cart-delete")
    Quantity_Dropdown = (By.CSS_SELECTOR, "#cart-quantity")

    def delete_item(self):
        self.click(*self.Delete_Button)

    def get_cart_items(self):
        return len(self.driver.find_elements(*self.CART_Item))

    def update_quantity(self,quantity):
        select = Select(self.driver.find_element(*self.Quantity_Dropdown))
        select.select_by_value(str(quantity))

#Step 3: We will write a pytest test case

def test_remove_from_cart(driver):
    cart = cartPage(driver)
    driver.get("https://www.amazon.com/gp/cart/view.html")
    initial_count = cart.get_cart_items()
    cart.delete_item()
    final_count = cart.get_cart_items()
    assert initial_count > final_count , "Item removed successfully from cart"

#Will follow page object model for clear seperation of test logic and UI interaction
#I will priortize automation for critical paths like adding, removing, quantity update, value verification
#I will use pytest fixtures for initializing the drivers and manage the sessions
#I will create html logging and add at every stage to analyze failures later

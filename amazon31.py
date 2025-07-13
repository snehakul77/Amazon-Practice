#Designing end to end user flow: Login -> Search -> Select -> add cart -> validate cart
from selenium.webdriver.common.by import By

from amazon17 import driver


#We will follow POM with logical seperation
#This will be the basepage which will include all the common functions which will be used in
# different scripts
class BasePage:
    def __init__(self,driver):
        self.driver = driver

    def click(self, by,locator):
        self.driver.find_element(by,locator).click()

    def type_text(self,by,locator,text):
        field = self.driver.find_element(by,locator)
        field.clear()
        field.send_keys(text)

    def capture_screenshot(self, name ="screenshot.png"):
        filename = f"screenshots/{name}_{datetime.now().strftime('%Y%m%d%H%M%S')}.png"
        self.driver.save_screenshot(filename)
        self.logger.info(f"Saved screenshot: {filename}")

#We will now create different files for different pages which will show the POM reference.
# Each file will have locators of that page and functions performed in that page

#Login Page:

class login_page(BasePage):
    EMAIL = (By.ID, "ap_email")
    PASSWORD = (By.ID, "ap_password")
    SIGN_IN = (By.ID, "ap_signin")

    def login(self,email,password):
        self.driver.find_element(*self.EMAIL).send_keys(email)
        self.driver.find_element(*self.PASSWORD).send_keys(password)
        self.driver.find_element(*self.SIGN_IN).click()

#Search Page

class search_page(BasePage):
    search_box = (By.ID, "search_box")

    def search(self,keyword):
        self.type_text(*self.search_box,keyword)
        self.driver.find_element(*self.search_box).submit()


#Product Page

class product_page(BasePage):
    ADD_TO_CART = (By.ID,"add_cart")

    def add_product_to_cart(self):
        self.click(*self.ADD_TO_CART)


#Cart Page

class cart_page(BasePage):
    CART_ITEM = (By.CSS_Selector,".sc-list-item")

    def is_item_in_cart(self):
        return len(self.driver.find_element(*self.CART_ITEM)) > 0

#Test Script for verifying E2E flow

def test_login_add_to_cart(driver,config):

    login = login_page(driver)
    search = search_page(driver)
    product = product_page(driver)
    cart = cart_page(driver)

    driver.get("https://www.amazon.in")
    login.login(config["Credentials"]["email"],config["Credentials"]["password"])
    self.capture_screenshot("login failure")

    search.search("mouse")
    driver.find_element(By.CSS_Selector,".sc-list-item").click()

    product.add_product_to_cart()
    driver.get("https://www.amazon.com/gp/cart/view.html")

    assert cart.is_item_in_cart(), 'Product not in cart'


#Config file will be as below

Credentials:
    Username: "snehakrishajhjhkd"
    Password: "<PASSWORD>"


#Reports can be generated using pytest html reports

#pytest --html-report.html


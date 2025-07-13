#E2E flow for api validation

#Framework structure

#Tests ---test_checkout_flow.py
#Utils --- api.helpers.py, config.py
#data --- testdata.json
#requirements.txt
#pytest.ini

#utils/api_helpers.py

import requests
base_url = "https://api.fakeecommerce.com"

def login_user(email,password):
    res = requests.post(f"{base_url}/auth/login",json = {"email" : email,"password":password})
    res.raise_for_status()
    return res.json()['token']

def search_products(token,keyword):
    headers = {"Authorization": f"Bearer {token}"}
    res = requests.get(f"{base_url}/products/search?q={keyword}",headers=headers)
    res.raise_for_status()
    return res.json()['results'][0]['id']

def add_to_cart(token,product_id):
    headers = {"Authorization": f"Bearer {token}"}
    res = requests.post(f"{base_url}/cart/add",headers=headers,json={"product_id":product_id,"quantity":1})
    res.raise_for_status()
    return res.status_code == 200

def checkout(token):
    headers = {"Authorization": f"Bearer {token}"}
    res = requests.post(f"{base_url}/checkout",headers=headers)
    res.raise_for_status()
    return res.json()


#-------------------------------

import pytest
from utils.api_helpers import *

def test_end_to_end_checkout():
    token = login_user("<EMAIL>","<PASSWORD>")
    product_id = search_products(token,"wireless headphones")
    add_to_cart(token,product_id)
    order = checkout(token)
    assert order["status"] == "confirmed"
    print("Order confirmed")
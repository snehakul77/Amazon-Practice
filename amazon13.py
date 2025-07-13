#API Automation
#code for simple get request

import requests

def test_get_users():
    url = "https://reqres.in/api/users/2"
    response = requests.get(url)

    print("Status code:", response.status_code)
    print("Response JSON:", response.json())

    assert response.status_code == 200
    assert response.headers["Content-Type"] == "application/json; charset=utf-8"

    data = response.json()

    assert "data" in data
    assert data["data"]["id"] == 2
    assert "email" in data["data"]
    assert "first_name" in data["data"]

    print("All checks passed for GET users")

test_get_users()


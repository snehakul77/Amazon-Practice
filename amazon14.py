#POST request for API automation

import requests

def test_create_user():
    url = "https://reqres.in/api/users"
    payload = {
        "name": "Sneha",
        "job" : "QA Engineer"
    }

    response = requests.post(url, json=payload)

    assert response.status_code == 401, f"Expected 201 , got {response.status_code}"
    assert response.headers["Content-Type"] == "application/json; charset=utf-8"

    data = response.json()
    print(data)

    assert data["name"] == "Sneha"
    assert data["job"] == "QA Engineer"
    assert "id" in data

    print("Post request tests passed")

test_create_user()

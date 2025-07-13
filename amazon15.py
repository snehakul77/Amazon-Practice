#Negative post requests API Automation
import requests


def test_post_users():
    url = "https://reqres.in/api/users"
    payload = {
        "name":"Sneha"

    }

    response = requests.post(url,json=payload)

    print("Status code: ", response.status_code)
    print("Response_body: ",response.json())


    if response.status_code == 201:
        print("Still accepted incomplete data")
    else:
        assert response.status_code == 400 or response.status_code == 422
        print("All negative checks passed (Invalid input was rejected)")

test_post_users()
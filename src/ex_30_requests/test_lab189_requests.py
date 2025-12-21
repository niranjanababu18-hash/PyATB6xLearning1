import requests
import json
import allure
import pytest
#function with test_ and filename as test_
base_url = "https://restful-booker.herokuapp.com"
headers = {
    "Content-Type": "application/json"
}

def get_token():
    base_path = "/auth"
    full_url = base_url + base_path
    payload = {
        "username": "admin",
        "password": "password123"
    }
    response = requests.post(url=full_url, json=payload, headers=headers)
    allure.attach(json.dumps(payload, indent=2), name="Request Payload", attachment_type=allure.attachment_type.JSON)
    allure.attach(response.text, name="Response Body", attachment_type=allure.attachment_type.JSON)
    response_json = response.json()
    token = response_json["token"]
    assert isinstance(token, str)
    assert len(token) > 0
    return token

def get_booking_id():
    base_path = "/booking"
    full_url = base_url + base_path
    payload = {
        "firstname": "Jim",
        "lastname": "Brown",
        "totalprice": 111,
        "depositpaid": True,
        "bookingdates": {
            "checkin": "2018-01-01",
            "checkout": "2019-01-01"
        },
        "additionalneeds": "Breakfast"
    }
    response = requests.post(url=full_url, json=payload, headers=headers)
    response_data = response.json()
    booking_id = response_data["bookingid"]
    return booking_id

@allure.title("TC#3 - Verify PUT request")
@allure.description("Update a booking and validate the response with Allure reporting")
@pytest.mark.positive
def test_put():
    token = get_token()
    bookingid = get_booking_id()
    base_path = "/booking/" + str(bookingid)
    full_url = base_url + base_path
    cookie = "token=" + token
    headers = {
        "Content-Type": "application/json",
        "Cookie": cookie
    }
    payload = {
        "firstname": "James",
        "lastname": "Brown",
        "totalprice": 222,
        "depositpaid": True,
        "bookingdates": {
            "checkin": "2020-01-01",
            "checkout": "2021-01-01"
        },
        "additionalneeds": "Lunch"
    }
    response = requests.put(url=full_url, json=payload, headers=headers)
    allure.attach(json.dumps(payload, indent=2), name="PUT Payload", attachment_type=allure.attachment_type.JSON)
    allure.attach(response.text, name="PUT Response Body", attachment_type=allure.attachment_type.JSON)
    assert response.status_code == 200
    assert response.json()["firstname"] == "James"
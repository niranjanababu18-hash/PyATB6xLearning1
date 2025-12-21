import requests
import json
import allure
import pytest

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

@allure.title("TC#4 - Verify DELETE request")
@allure.description("Delete a booking and validate the response with Allure reporting")
@pytest.mark.positive
def test_delete():
    token = get_token()
    bookingid = get_booking_id()
    base_path = "/booking/" + str(bookingid)
    full_url = base_url + base_path
    cookie = "token=" + token
    headers = {
        "Content-Type": "application/json",
        "Cookie": cookie
    }

    # Send DELETE request
    response = requests.delete(url=full_url, headers=headers)
    allure.attach(response.text or "No body", name="DELETE Response Body", attachment_type=allure.attachment_type.TEXT)

    # Validate response
    assert response.status_code == 201  # Restful Booker returns 201 on successful delete

    # Double-check: try to GET the deleted booking
    get_response = requests.get(url=full_url, headers=headers)
    assert get_response.status_code == 404

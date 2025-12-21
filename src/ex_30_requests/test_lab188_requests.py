import requests
import json
import allure
import pytest
@allure.title("TC#3 - Verify POST request")
@allure.description("Send a POST request and validate the response with Allure reporting")
@pytest.mark.positive
def test_post_request():
    base_url = "https://restful-booker.herokuapp.com"
    base_path="/auth"
    full_url=base_url+base_path
    payload = payload = {
    "username": "admin",
    "password": "password123"
}
    headers = {
        "Content-Type": "application/json"
    }
    # Send POST request
    response_data = requests.post(url=full_url, json=payload, headers=headers)
    print(response_data)
    allure.attach(json.dumps(payload, indent=2), name="Request Payload", attachment_type=allure.attachment_type.JSON)
    allure.attach(response_data.text, name="Response Body", attachment_type=allure.attachment_type.JSON)
    response_json = response_data.json()
    token=response_json["token"]
    print(token)
    assert type(token) == str
    assert len(token) > 0



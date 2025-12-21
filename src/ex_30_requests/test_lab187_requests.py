import pytest
import allure
import requests
import json
@allure.title("TC#2 - Verify POST request")
@allure.description("Send a POST request and validate the response with Allure reporting")
@pytest.mark.positive
def test_post_request():
    base_url = "https://restful-booker.herokuapp.com"
    base_path="/booking"
    full_url=base_url+base_path
    payload = {
    "firstname" : "Jim",
    "lastname" : "Brown",
    "totalprice" : 111,
    "depositpaid" : True,
    "bookingdates" : {
        "checkin" : "2018-01-01",
        "checkout" : "2019-01-01"
    },
    "additionalneeds" : "Breakfast"
}
    headers = {
        "Content-Type": "application/json"
    }

    # Send POST request
    response_data = requests.post(url=full_url, json=payload, headers=headers)
 #   print(response_data.text)
    # Attach request and response details to Allure report
    allure.attach(json.dumps(payload, indent=2),
                  name="Request Payload",
                  attachment_type=allure.attachment_type.JSON)

    allure.attach(response_data.text,
                  name="Response Body",
                  attachment_type=allure.attachment_type.JSON)
    response_json = response_data.json()
    Total = response_json["booking"]["totalprice"]
    print(Total)
    # Assertions
    assert response_data.status_code == 200
    assert Total == payload["totalprice"]

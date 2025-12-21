import pytest
import allure
import requests
@allure.title("TC#1-verify the GET request")
@allure.description("Verify the GET request")
@pytest.mark.positive
def test_new_get_request():
    url="https://restful-booker.herokuapp.com/booking/1"
    response_data=requests.get(url=url)
    assert response_data.status_code == 200
    print("Hello World")
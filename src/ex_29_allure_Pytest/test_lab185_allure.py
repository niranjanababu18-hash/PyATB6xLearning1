#allure has inbuilt method for HTML report creation
import pytest
import allure
allure.title("create booking is verifying or not")
@pytest.mark.positive
def test_create_booking_positive():
    print("test1")
    assert 1+1==2
allure.title("create booking is verifying or not")
@pytest.mark.negative
def test_create_booking_negative():
    print("test2")
    assert 1-1==2

@pytest.mark.positive
def test_create_booking_positive2():
    print("test3")
    assert 1+1==2
@pytest.mark.negative
def test_create_booking_negative2():
    print("test4")
    assert 1-1==2

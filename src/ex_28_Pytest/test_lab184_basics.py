import pytest
#marking to understand its a pytest
@pytest.mark.smoke
def test_method():
    print("Hello World")
    assert 5==5
@pytest.mark.smoke
def test_method1():
    print("Hello world1")
    assert 5==6
#pytest is calling the method
@pytest.mark.smoke
def test_login():
    print("test")
    assert 1+1==2
#pytest -v
#pytest -vv
#pytest -q
#pytest -s


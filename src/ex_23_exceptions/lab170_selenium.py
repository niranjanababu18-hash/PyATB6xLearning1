from selenium.common.exceptions import NoSuchElementException
from selenium import webdriver
from selenium.webdriver.common.by import By

try:
    driver = webdriver.Chrome()
    driver.get("https://www.example.com")
    driver.find_element(by=By.NAME, value="q")
except NoSuchElementException as e:
    print("No such element",e.msg)
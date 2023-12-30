import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By

driver = webdriver.Chrome()


@pytest.fixture(autouse=True)
def set_up():
    driver.get("https://the-internet.herokuapp.com/login")
    driver.maximize_window()

"""
def test_app_title():
    assert driver.title == "The Internet"
    print(driver.title)
"""



def test_valid_login():
    ## test steps
    driver.find_element(By.ID, "username").send_keys("tomsmith")
    driver.find_element(By.ID, "password").send_keys("SuperSecretPassword!")
    driver.find_element(By.CSS_SELECTOR, "button.radius").click()

    ## test result
    actual_text = driver.find_element(By.ID, "flash").text
    assert actual_text.__contains__("You logged into a secure area!")


"""
def test_invalid_username():
    driver.find_element(By.ID, "username").send_keys("5345345453")
    driver.find_element(By.ID, "password").send_keys("SuperSecretPassword!")
    driver.find_element(By.CSS_SELECTOR, "button.radius").click()

    actual_text = driver.find_element(By.ID, "flash").text
    assert actual_text.__contains__("Your username is invalid!")


def test_invalid_password():
    driver.find_element(By.ID, "username").send_keys("tomsmith")
    driver.find_element(By.ID, "password").send_keys("**#$%Yrerwer123")
    driver.find_element(By.CSS_SELECTOR, "button.radius").click()

    actual_text = driver.find_element(By.ID, "flash").text
    assert actual_text.__contains__("Your password is invalid!")
"""

test_data = [("", "", "Your username is invalid!"), ("", "SuperSecretPassword!", "Your username is invalid!"),
             ("tomsmith", "", "Your password is invalid!")]


@pytest.mark.parametrize("us_name,password,expected_message", test_data)
def test_invalid_login(us_name, password, expected_message):
    driver.find_element(By.ID, "username").send_keys(us_name)
    driver.find_element(By.ID, "password").send_keys(password)
    driver.find_element(By.CSS_SELECTOR, "button.radius").click()

    actual_text = driver.find_element(By.ID, "flash").text
    assert actual_text.__contains__(expected_message)

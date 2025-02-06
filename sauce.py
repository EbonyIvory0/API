import pytest
from selenium.webdriver.common.by import By
from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
import selenium.webdriver.support.expected_conditions as EC
import time

browser = webdriver.Chrome()
wait = WebDriverWait(browser, 10)
LINK = "https://www.saucedemo.com"
browser.get(LINK)

@pytest.mark.skip
def test_correct_input():
    wait.until(
        EC.presence_of_element_located((By. ID, "user-name"))
    ).send_keys("standard_user")
    browser.find_element(By. ID, "password").send_keys("secret_sauce")
    browser.find_element(By. ID, "login-button").click()
    time.sleep(1)
    check = wait.until(
        EC.presence_of_element_located((By. CSS_SELECTOR, "[data-test='title']"))
    )
    assert check.text == "Products", "LLLL"
    browser.delete_all_cookies()
    browser.refresh()

def test_incorrect_input():
    time.sleep(1)
    wait.until(
        EC.presence_of_element_located((By. ID, "user-name"))
    ).send_keys("stan")
    browser.find_element(By. ID, "password").send_keys("secret_sauce")
    browser.find_element(By. ID, "login-button").click()
    time.sleep(1)
    check = wait.until(
        EC.presence_of_element_located((By. TAG_NAME, "h3"))
    )
    assert check.text == "Epic sadface: Username and password do not match any user in this service", "LLLL"
    time.sleep(2)

def test_empty_password():
    browser.delete_all_cookies()
    wait.until(
        EC.presence_of_element_located((By. ID, "user-name"))
    ).clear()
    wait.until(
    EC.presence_of_element_located((By. ID, "user-name"))
    ).send_keys("standard_user")
    time.sleep(3)
    browser.find_element(By. ID, "password").clear()
    # browser.find_element(By. ID, "password").send_keys("")
    browser.find_element(By. ID, "login-button").click()
    time.sleep(1)
    check = wait.until(
        EC.presence_of_element_located((By. TAG_NAME, "h3"))
    )
    assert check.text == "Epic sadface: Password is required"
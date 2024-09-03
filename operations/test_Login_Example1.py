import allure
import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By


@pytest.fixture
def test_setUp():
    global driver
    driver = webdriver.Chrome()
    driver.get("https://opensource-demo.orangehrmlive.com/web/index.php/auth/login")
    driver.maximize_window()
    driver.implicitly_wait(30)
    yield
    driver.close()


@allure.description("Valid OrangeHRM Login Credentials")
@allure.severity(severity_level='CRITICAL')
def test_validCredentials(test_setUp):
    driver.find_element(By.NAME, "username").send_keys("Admin")
    driver.find_element(By.NAME, "password").send_keys("admin123")
    driver.find_element(By.XPATH, "//button[normalize-space(text()='Login')]").click()
    dashboard_text = driver.find_element(By.XPATH, "//h6[text()='Dashboard']").text
    assert dashboard_text == "Dashboard"


@allure.description("Invalid OrangeHRM Login Credentials")
@allure.severity(severity_level='NORMAL')
def test_invalidCredentials(test_setUp):
    driver.find_element(By.NAME, "username").send_keys("Admin")
    driver.find_element(By.NAME, "password").send_keys("admin12")
    driver.find_element(By.XPATH, "//button[normalize-space(text()='Login')]").click()
    dashboard_text = driver.find_element(By.XPATH, "//h6[text()='Dashboard']").text
    try:
        assert dashboard_text == "Dashboard"
    finally:
        if AssertionError:
            allure.attach(driver.get_screenshot_as_png(),name="Invalid Credentials", attachment_type= allure.attachment_type.PNG)

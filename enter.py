import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time

@pytest.fixture(scope="module")
def setup():
    driver = webdriver.Chrome()
    driver.get("https://office.easyhrm.online/index.php")
    driver.maximize_window()
    yield driver
    driver.quit()

def test_login(setup):
    driver = setup
    try:
        mobile_input = WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.XPATH, "//input[@name='mobile']")))
        mobile_input.send_keys("01961930719")
        
        password_input = WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.XPATH, "//input[@name='password']")))
        password_input.send_keys("1")
        
        role_select = WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.XPATH, "//div[1]/form/div[3]/select")))
        role_select.click()
        role_option = WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.XPATH, "//div[1]/form/div[3]/select/option[2]")))
        role_option.click()
        
        remarks_input = WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.XPATH, "//input[@name='remarks']")))
        remarks_input.send_keys("")
        
        login_button = WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.XPATH, "//button[@class='btn btn-success']")))
        login_button.click()
        
        time.sleep(2)
        driver.save_screenshot('./screenshots/enter.png')
        print("Print : Captured Screenshot")
        print("Success: Script executed without errors.")
    except Exception as e:
        print(f"Failed: {e}")
        pytest.fail("Test failed due to an exception.")
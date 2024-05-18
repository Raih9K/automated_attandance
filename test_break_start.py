import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By
import time

# Fixture for setting up and tearing down the WebDriver
@pytest.fixture(scope="function")
def driver():
    driver = webdriver.Chrome()
    driver.maximize_window()
    yield driver
    driver.quit()

def logindata(driver, username, password):
    driver.find_element(By.XPATH, "//input[@name='mobile']").send_keys(username)
    driver.find_element(By.XPATH, "//input[@name='password']").send_keys(password)

def test_break_start(driver):
    driver.get("https://office.easyhrm.online/index.php")

    try:
        logindata(driver, "01961930718", "1")

        driver.find_element(By.XPATH, "//div[1]/form/div[3]/select/option[4]").click()
        driver.find_element(By.XPATH, "//input[@name='remarks']").send_keys("")
        driver.find_element(By.XPATH, "//button[@class='btn btn-success']").click()
        time.sleep(2)
        driver.save_screenshot('./screenshots/break_start.png')
        print("Print: Captured Screenshot")
        print("Success: Script executed without errors.")
    except Exception as e:
        print(f"Failed: {e}")
        pytest.fail("Test failed due to exception.")

if __name__ == "__main__":
    pytest.main()

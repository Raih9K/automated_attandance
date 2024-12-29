import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import time

@pytest.fixture(scope="module")
def browser():
    # Set up the browser (Chrome in this case)
    driver = webdriver.Chrome()  # Make sure you have the ChromeDriver in your PATH
    yield driver
    driver.quit()

def test_google_search(browser):
    # Navigate to Google
    browser.get("https://www.google.com")

    # Find the search box using its name attribute value
    search_box = browser.find_element(By.NAME, "q")

    # Type "raihan khan SQA" in the search box
    search_box.send_keys("raihan khan SQA")

    # Press Enter to submit the search
    search_box.send_keys(Keys.RETURN)

    # Wait for a few seconds to allow results to load
    time.sleep(3)

    # Check if the results page contains the search term
    assert "raihan khan SQA" in browser.title

    # Optionally, you can check for specific elements in the results
    results = browser.find_elements(By.CSS_SELECTOR, 'h3')
    assert len(results) > 0  # Ensure there are search results

if __name__ == "__main__":
    pytest.main()
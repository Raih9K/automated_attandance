from selenium import webdriver
from selenium.webdriver.common.by import By
import time

driver = webdriver.Chrome()
driver.get("https://office.easyhrm.online/index.php")
driver.maximize_window()
try:
    driver.find_element(
        By.XPATH, "//input[@name='mobile']").send_keys("01961930719")
    driver.find_element(
        By.XPATH, "//input[@name='password']").send_keys("1")
    driver.find_element(
        By.XPATH, "//div[1]/form/div[3]/select/option[5]").click()
    driver.find_element(
        By.XPATH, "//input[@name='remarks']").send_keys("")
    driver.find_element(By.XPATH, "//button[@class='btn btn-success']").click()
    time.sleep(10)
    driver.save_screenshot('./screenshots/break_end.png')
    print("Print : Captured Screenshot")
    print("Success: Script executed without errors.")
except:
    print("Failed")

driver.quit()

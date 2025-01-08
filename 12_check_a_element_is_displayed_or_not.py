import time
from selenium import webdriver
from selenium.webdriver.common.by import By

driver = webdriver.Chrome()
driver.maximize_window()
driver.get("https://tutorialsninja.com/demo/")
time.sleep(3)

driver.find_element(By.XPATH,"//span[text()='My Account']").click()
time.sleep(3)

driver.find_element(By.LINK_TEXT,"Login").click()
time.sleep(3)

driver.find_element(By.XPATH,"//input[@name='email']").send_keys("sqaengineerrubel@gmail.com")
time.sleep(3)

driver.find_element(By.XPATH,"//input[@name='password']").send_keys("123456")
time.sleep(3)

driver.find_element(By.XPATH,"//input[@value='Login']").click()
time.sleep(3)

if driver.find_element(By.LINK_TEXT,"Edit your account information").is_displayed():
    print("Login successfully")

else:
    print("Failed")
















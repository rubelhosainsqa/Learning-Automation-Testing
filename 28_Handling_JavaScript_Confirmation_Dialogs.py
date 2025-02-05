import time
from selenium import webdriver
from selenium.webdriver.common.by import By

driver = webdriver.Chrome()
driver.maximize_window()
driver.get("https://the-internet.herokuapp.com/javascript_alerts")
time.sleep(5)

driver.find_element(By.XPATH,"//button[text()='Click for JS Confirm']").click()
time.sleep(5)

confirmation_alert = driver.switch_to.alert
print(confirmation_alert.text)
# confirmation_alert.accept()
confirmation_alert.dismiss()

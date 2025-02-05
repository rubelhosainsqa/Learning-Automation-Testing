import time
from selenium import webdriver
from selenium.webdriver.common.by import By

driver = webdriver.Chrome()
driver.maximize_window()
driver.get("https://the-internet.herokuapp.com/javascript_alerts")
time.sleep(5)

driver.find_element(By.XPATH,"//button[text()='Click for JS Prompt']").click()
time.sleep(5)

prompt_alert = driver.switch_to.alert
print(prompt_alert.text)

prompt_alert.send_keys("I am Rubel Hosain")
time.sleep(5)
prompt_alert.accept()

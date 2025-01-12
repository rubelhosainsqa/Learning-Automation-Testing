
import time
from selenium import webdriver
from selenium.webdriver.common.by import By


driver = webdriver.Chrome()
driver.maximize_window()
driver.get("https://the-internet.herokuapp.com/")
time.sleep(3)


driver.find_element(By.LINK_TEXT,"JavaScript Alerts").click()
time.sleep(3)
driver.find_element(By.XPATH,"//button[text()='Click for JS Alert']").click()
time.sleep(3)


alert = driver.switch_to.alert
print(alert.text)
alert.accept()
#alert.dismiss()


driver.find_element(By.LINK_TEXT,"Elemental Selenium").click()
time.sleep(3)
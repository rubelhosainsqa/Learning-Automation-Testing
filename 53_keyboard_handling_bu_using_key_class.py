import time
from selenium import webdriver
from selenium.webdriver import ActionChains, Keys
from selenium.webdriver.common.by import By

driver = webdriver.Chrome()
driver.maximize_window()
driver.get("https://tutorialsninja.com/demo/index.php?route=account/login")
time.sleep(5)

driver.find_element(By.NAME,"email").send_keys("rh.riyon.bd@gmail.com")
time.sleep(5)
driver.find_element(By.NAME,"password").send_keys("allahprotectme#1")
time.sleep(5)

# Handling keyboard by using key class
# driver.find_element(By.NAME,"password").send_keys(Keys.ENTER) # This is a technique for press keyboard button
# time.sleep(5)

# Handling keyboard by using action chains
action = ActionChains(driver)
action.send_keys(Keys.ENTER)
time.sleep(5)















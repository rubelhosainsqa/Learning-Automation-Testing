import time
from selenium import webdriver

driver = webdriver.Chrome()
driver.maximize_window()
driver.get("https://tutorialsninja.com/demo/index.php?route=account/login")
time.sleep(5)

driver.execute_script("alert('Rubel')")

time.sleep(5)
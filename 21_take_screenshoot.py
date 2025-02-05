import time
from selenium import webdriver
from selenium.webdriver.common.by import By

driver = webdriver.Chrome()
driver.maximize_window()
driver.get("https://tutorialsninja.com/demo/index.php?route=account/login")
time.sleep(5)

# Technique 1
driver.save_screenshot("image.png")

# Technique 2
driver.get_screenshot_as_file("C:\\Users\\Rubel\\Documents\\Automation_Testing\\Screenshoot\\pic.png")

# Technique 3
icon = driver.find_element(By.XPATH,"//button[@class='btn btn-default btn-lg']")
icon.screenshot("search.png")

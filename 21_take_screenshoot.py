import time
from selenium import webdriver

driver = webdriver.Chrome()
driver.maximize_window()
driver.get("https://tutorialsninja.com/demo/index.php?route=account/login")
time.sleep(5)

driver.save_screenshot("image.png") 
driver.get_screenshot_as_file("C:\\Users\\Rubel\\Documents\\Automation_Testing\\Screenshoot\\pic.png")

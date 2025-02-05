import time
from selenium import webdriver

# Open the window as a full screen by using ChromeOptions()
'''
chrome_options = webdriver.ChromeOptions()
chrome_options.add_argument("--kiosk")
driver = webdriver.Chrome(options=chrome_options)

'''
# Open the window as a full screen by using generally
driver = webdriver.Chrome()
driver.get("https://tutorialsninja.com/demo/index.php?route=account/login")
driver.fullscreen_window()
time.sleep(5)
import time
from selenium import webdriver

chrome_options = webdriver.ChromeOptions()
chrome_options.add_argument("--start-maximized")
driver = webdriver.Chrome(options=chrome_options)

driver.get("https://tutorialsninja.com/demo/index.php?route=account/login")
time.sleep(5)
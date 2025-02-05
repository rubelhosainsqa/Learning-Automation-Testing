import time
from selenium import webdriver

chrome_option = webdriver.ChromeOptions()
chrome_option.add_argument("--headless")

driver = webdriver.Chrome(options=chrome_option)
driver.maximize_window()
driver.get("https://tutorialsninja.com/demo/index.php?route=account/login")
time.sleep(5)

title = driver.title
print(title)

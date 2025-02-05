import time
from selenium import webdriver
from selenium.webdriver.chrome.options import Options

chrome_options = Options()
chrome_options.add_experimental_option("excludeSwitches",["enable-automation"])
chrome_options.add_experimental_option("useAutomationExtension", False)
chrome_options.add_argument('--disable-blink-features=AutomationControlled')

driver = webdriver.Chrome(options=chrome_options)
driver.maximize_window()

driver.get("https://tutorialsninja.com/demo/")
time.sleep(10)
print(driver.title)


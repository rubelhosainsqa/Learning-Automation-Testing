import time
from selenium import webdriver
from selenium.webdriver.ie.options import Options

chrome_option = Options()
chrome_option.add_argument("--disable-notifications")

driver = webdriver.Chrome(options=chrome_option)
driver.maximize_window()
driver.get("https://the-internet.herokuapp.com/")
time.sleep(3)

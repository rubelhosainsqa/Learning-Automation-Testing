import time
from selenium import webdriver

driver = webdriver.Chrome()
driver.maximize_window()
driver.get("https://omayo.blogspot.com/")
time.sleep(5)

driver.execute_script("window.scrollTo(0,2499)")
time.sleep(5)
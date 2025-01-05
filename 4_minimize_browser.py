import time
from selenium import webdriver

driver = webdriver.Chrome()
time.sleep(5) # Time used for waiting
driver.maximize_window()
driver.get("https://atb-jobs.com/")
time.sleep(5)
driver.minimize_window()  # minimize_window() used for browser minimize
time.sleep(5)
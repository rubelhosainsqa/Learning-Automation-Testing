import time
from selenium import webdriver
from selenium.webdriver.common.by import By

driver = webdriver.Chrome()
driver.maximize_window()
driver.get("https://omayo.blogspot.com/")
time.sleep(3)

tab1 = driver.current_url # current_url is used for copy the browser current url
print(tab1)
time.sleep(3)

driver.find_element(By.LINK_TEXT,"onlytestingblog").click()
tab2 = driver.current_url
print(tab2)
time.sleep(3)
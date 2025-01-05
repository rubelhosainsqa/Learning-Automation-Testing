import time
from selenium import webdriver
from selenium.webdriver.common.by import By

driver = webdriver.Chrome()
driver.maximize_window()
driver.get("https://omayo.blogspot.com/")
time.sleep(3)

tab1 = driver.title # title is used for copy the browser tab title
print(tab1)
time.sleep(3)

driver.find_element(By.LINK_TEXT23,"onlytestingblog").click()
tab2 = driver.title
print(tab2)
time.sleep(3)
import time
from selenium import webdriver
from selenium.webdriver.common.by import By

driver = webdriver.Chrome()
driver.maximize_window()
time.sleep(3)
driver.get("https://omayo.blogspot.com/")

tagname = driver.find_element(By.ID,"pah").tag_name # tag_name is used for copy the located element html tag
print(tagname)
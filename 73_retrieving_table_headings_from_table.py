import time
from selenium import webdriver
from selenium.webdriver.common.by import By

driver = webdriver.Chrome()
driver.maximize_window()
driver.get("https://omayo.blogspot.com/")
time.sleep(5)

table_head = driver.find_elements(By.XPATH,"//table[@id='table1']/thead/tr/th")

for data in table_head:
    print(data.text)


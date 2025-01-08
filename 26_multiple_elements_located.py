import time
from selenium import webdriver
from selenium.webdriver.common.by import By

driver = webdriver.Chrome()
driver.maximize_window()
time.sleep(3)
driver.get("https://omayo.blogspot.com/")

dropdown_list = driver.find_elements(By.XPATH,"//select[@id='multiselect1']/option")

print(len(dropdown_list))

for a in dropdown_list:
    print(a.text)


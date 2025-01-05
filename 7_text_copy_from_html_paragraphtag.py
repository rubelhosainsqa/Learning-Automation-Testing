import time
from selenium import webdriver
from selenium.webdriver.common.by import By

driver = webdriver.Chrome()
driver.maximize_window()
time.sleep(3)
driver.get("https://omayo.blogspot.com/")

text_copy1 = driver.find_element(By.ID,"pah").text # .text is used for copy text
print(text_copy1)

text_copy2 = driver.find_element(By.ID,"post-body-9023929218208337252").text
print(text_copy2)

text_copy3 = driver.find_element(By.XPATH,"//h2[normalize-space()='Text Area Field']").text
print(text_copy3)

text_copy4 = driver.find_element(By.XPATH,"//button[normalize-space()='Submit']").text
print(text_copy4)
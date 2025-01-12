import time
from selenium import webdriver
from selenium.webdriver.common.by import By

driver = webdriver.Chrome()
driver.maximize_window()
driver.get("https://practice-automation.com/modals/")
time.sleep(5)

driver.find_element(By.ID, "simpleModal").click()
time.sleep(5)

Head_title = driver.find_element(By.ID,"pum_popup_title_1318")
print(Head_title.text)
time.sleep(5)

Second_title = driver.find_element(By.XPATH,"//div[@id='pum_popup_title_1318']/following::p")
print(Second_title.text)
time.sleep(5)

driver.find_element(By.XPATH,"(//button[@class='pum-close popmake-close'])[2]").click()
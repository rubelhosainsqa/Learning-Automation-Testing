import time
from selenium import webdriver
from selenium.webdriver import ActionChains
from selenium.webdriver.common.by import By

driver = webdriver.Chrome()
driver.maximize_window()
driver.get("https://omayo.blogspot.com/")
time.sleep(5)

# Generally used this process
# driver.find_element(By.ID,"link2").click()

# Mouse left button clicking by using ActionChains object

button = driver.find_element(By.ID,"link2")
action = ActionChains(driver)
action.click(button).perform()
import time
from selenium import webdriver
from selenium.webdriver import ActionChains
from selenium.webdriver.common.by import By

driver = webdriver.Chrome()
driver.maximize_window()
driver.get("https://tutorialsninja.com/demo/")
time.sleep(5)

# Mouse right button clicking by using ActionChains object
search = driver.find_element(By.NAME,"search")
action = ActionChains(driver)
action.context_click(search).perform()
time.sleep(10)
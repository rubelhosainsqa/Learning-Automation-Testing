import time
from selenium import webdriver
from selenium.webdriver import ActionChains, Keys
from selenium.webdriver.common.by import By

driver = webdriver.Chrome()
driver.maximize_window()
driver.get("https://omayo.blogspot.com/")
time.sleep(5)

button = driver.find_element(By.LINK_TEXT,"compendiumdev")

action = ActionChains(driver)
action.key_down(Keys.CONTROL).click(button).key_up(Keys.CONTROL).perform()
time.sleep(5)


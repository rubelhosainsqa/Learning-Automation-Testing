import time
from selenium import webdriver
from selenium.webdriver import ActionChains
from selenium.webdriver.common.by import By

driver = webdriver.Chrome()
driver.maximize_window()
driver.get("https://omayo.blogspot.com/p/page3.html")
time.sleep(5)

slider = driver.find_element(By.XPATH,"//a[@class='ui-slider-handle ui-btn ui-shadow ui-btn-null'][1]")

action = ActionChains(driver)
action.drag_and_drop_by_offset(slider,100,0).perform()
time.sleep(5)

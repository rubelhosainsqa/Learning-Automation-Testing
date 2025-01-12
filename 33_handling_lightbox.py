import time
from selenium import webdriver
from selenium.webdriver.common.by import By

driver = webdriver.Chrome()
driver.maximize_window()
driver.get("https://tutorialsninja.com/demo/index.php?route=product/product&path=57&product_id=49")
time.sleep(5)

driver.find_element(By.XPATH,"(//a[@title='Samsung Galaxy Tab 10.1'])[1]").click()
time.sleep(5)
driver.find_element(By.XPATH,"//button[@class='mfp-close']").click()
time.sleep(5)
driver.quit()
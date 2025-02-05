import time
from selenium import webdriver
from selenium.webdriver.common.by import By

driver = webdriver.Chrome()
driver.maximize_window()
driver.get("https://omayo.blogspot.com/")
time.sleep(5)

# Click by using selenium
# driver.find_element(By.ID,"alert1").click()

# Click by using javascript
driver.execute_script("document.getElementById('alert1').click()")
time.sleep(5)
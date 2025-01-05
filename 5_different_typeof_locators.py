import time
from selenium import webdriver
from selenium.webdriver.common.by import By

driver = webdriver.Chrome()
driver.maximize_window()
driver.get("https://omayo.blogspot.com/")
time.sleep(5)

# Locate an element by ID and inputting some text in the search input field by using send keys
driver.find_element(By.ID,"ta1").send_keys("I am Rubel Hosain")
time.sleep(5)

# Locate an element by Name and inputting some text in the search input field by using send keys
driver.find_element(By.NAME,"q").send_keys("Dummy Text")
time.sleep(5)

# Locate an element by Link Text and click the link text
#driver.find_element(By.LINK_TEXT,"http://www.Selenium143.blogspot.com").click()
#time.sleep(5)

# Locate an element by ID and click the on the redio button
driver.find_element(By.ID,"radio2").click()
time.sleep(5)

# Locate an element by ID and click the on the checkmark
driver.find_element(By.ID,"checkbox2").click()
time.sleep(5)

# Locate the dropdown element by using Xpath and click the dropdown
driver.find_element(By.XPATH, "//select[@id='drop1']").click()
time.sleep(5)

# Locate a value from the dropdown list and click the dropdown
driver.find_element(By.ID, "ironman4").click()
time.sleep(5)
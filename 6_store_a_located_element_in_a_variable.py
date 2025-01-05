import time
from selenium import webdriver
from selenium.webdriver.common.by import By

driver = webdriver.Chrome()
driver.maximize_window()
time.sleep(3)
driver.get("https://omayo.blogspot.com/")

# Located the search field and store a variable
input_field = driver.find_element(By.ID, "textbox1")
input_field.clear() # Clear() is used for clear the search field
time.sleep(3)

input_field.send_keys("Rubel")
input_field.clear()
time.sleep(3)

input_field.send_keys("Hosain")
input_field.clear()
time.sleep(3)

driver.quit()  # quit() is used for close the driver
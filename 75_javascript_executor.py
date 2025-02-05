import time
from selenium import webdriver


driver = webdriver.Chrome()
driver.maximize_window()
driver.get("https://omayo.blogspot.com/")
time.sleep(5)


# driver.execute_script("alert('Rubel')")
# driver.execute_script("prompt('Rubel')")
driver.execute_script("confirm('Rubel')")
time.sleep(5)
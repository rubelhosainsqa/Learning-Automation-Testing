import time
from selenium import webdriver


driver = webdriver.Chrome()
driver.maximize_window()
driver.get("https://omayo.blogspot.com/")
time.sleep(5)


driver.switch_to.new_window('window')
driver.get("https://www.facebook.com/")
time.sleep(5)


driver.switch_to.new_window('tab')
driver.get("https://www.youtube.com/")
time.sleep(5)

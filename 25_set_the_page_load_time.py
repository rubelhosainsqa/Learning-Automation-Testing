
from selenium import webdriver

driver = webdriver.Chrome()
driver.maximize_window()
driver.set_page_load_timeout(5)
driver.get("https://omayo.blogspot.com/")
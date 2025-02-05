import time
from selenium import webdriver

driver = webdriver.Chrome()
driver.maximize_window()
driver.get("https://seleniumpractise.blogspot.com/2016/08/how-to-handle-calendar-in-selenium.html")

# Select future date
# driver.execute_script("document.getElementById('datepicker').value='15/01/2027'")

# Select past date
driver.execute_script("document.getElementById('datepicker').value='15/01/2021'")

time.sleep(5)
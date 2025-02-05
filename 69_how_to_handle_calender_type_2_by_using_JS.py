import time
from selenium import webdriver

driver = webdriver.Chrome()
driver.maximize_window()
driver.get("https://www.path2usa.com/travel-companion/")
time.sleep(5)

# Select Past Date
# driver.execute_script("document.getElementById('form-field-travel_comp_date').value='15/01/2021'")

# Select Future Date
driver.execute_script("document.getElementById('form-field-travel_comp_date').value='15/01/2027'")
time.sleep(5)
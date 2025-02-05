import time
from selenium import webdriver
from selenium.webdriver import ActionChains, Keys
from selenium.webdriver.common.by import By

driver = webdriver.Chrome()
driver.maximize_window()
driver.get("https://www.makemytrip.com/")
time.sleep(5)

# Close the add pop up
driver.find_element(By.XPATH,"//span[@class='commonModal__close']").click()
time.sleep(5)


driver.find_element(By.ID,"fromCity").click()
time.sleep(5)

# Located the search field and type KO for search
driver.find_element(By.XPATH,"//input[@class='react-autosuggest__input react-autosuggest__input--open']").send_keys("Ko")
time.sleep(5)

# Select anyone from the suggestive dropdown list
action = ActionChains(driver)
action.send_keys(Keys.ARROW_DOWN).send_keys(Keys.ARROW_DOWN).send_keys(Keys.ARROW_DOWN).send_keys(Keys.ENTER).perform()
time.sleep(5)
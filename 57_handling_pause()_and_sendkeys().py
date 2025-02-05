import time
from selenium import webdriver
from selenium.webdriver import ActionChains, Keys
from selenium.webdriver.common.by import By

driver = webdriver.Chrome()
driver.maximize_window()
driver.get("https://tutorialsninja.com/demo/index.php?route=account/register")
time.sleep(5)

driver.find_element(By.NAME,"firstname").send_keys("Rubel")
time.sleep(5)

action = ActionChains(driver)
action.send_keys(Keys.TAB).pause(3).send_keys("Hosain").send_keys(Keys.TAB).pause(3).send_keys("rh.riyon@gmail.com").send_keys(Keys.TAB).perform()
time.sleep(5)


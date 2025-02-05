from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait

driver = webdriver.Chrome()
driver.get("https://omayo.blogspot.com/")
driver.maximize_window()

driver.find_element(By.ID,"alert1").click()

# Wait mechanism >> Explicit wait system with condition alert_is_present() it will be wait for alert popup
wait =  WebDriverWait(driver,5)
wait.until(expected_conditions.alert_is_present())

alert_text = driver.switch_to.alert.text
print(alert_text)



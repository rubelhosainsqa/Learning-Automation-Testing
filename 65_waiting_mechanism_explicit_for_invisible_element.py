from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait

driver = webdriver.Chrome()
driver.get("https://the-internet.herokuapp.com/dynamic_loading/1")
driver.maximize_window()

driver.find_element(By.XPATH,"//button[text()='Start']").click()

# Wait mechanism >> Explicit wait system with condition invisibility_of_element_located it will be handel invisible aelement
wait =  WebDriverWait(driver,30)
loader = wait.until(expected_conditions.invisibility_of_element_located((By.ID,"loading")))

hello_text = driver.find_element(By.XPATH,"//div[@id='finish']").text
print(hello_text)


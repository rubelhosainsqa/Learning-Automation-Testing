import time
from selenium import webdriver
from selenium.webdriver.common.by import By

driver = webdriver.Chrome()
driver.maximize_window()
driver.get("https://letcode.in/frame")
time.sleep(5)

driver.switch_to.frame("firstFr")

driver.find_element(By.NAME,"fname").send_keys("Rubel ")
driver.find_element(By.NAME,"lname").send_keys("Hosain")
time.sleep(5)

child_frame = driver.find_element(By.XPATH,"//iframe[@class='has-background-white']")
driver.switch_to.frame(child_frame)

driver.find_element(By.NAME,"email").send_keys("rh.riyon.bd@gmail.com")
time.sleep(5)
driver.find_element(By.NAME,"email").clear()
time.sleep(5)

driver.switch_to.parent_frame()
driver.find_element(By.NAME,"fname").clear()
driver.find_element(By.NAME,"lname").clear()
time.sleep(5)

driver.switch_to.default_content()
head_text = driver.find_element(By.XPATH,"//h1[@class='title is-title is-size-1-desktop is-size-3-mobile is-size-2-tablet has-text-weight-bold has-text-primary']")
print(head_text.text)
time.sleep(5)
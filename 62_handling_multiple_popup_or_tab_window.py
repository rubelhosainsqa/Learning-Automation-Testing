import time
from selenium import webdriver
from selenium.webdriver.common.by import By


driver = webdriver.Chrome()
driver.maximize_window()
driver.get("https://omayo.blogspot.com/")
time.sleep(5)


parent_window = driver.current_window_handle  #Current parent window capture hobe


driver.find_element(By.XPATH,"//a[text()='Open a popup window']").click()


all_windows = driver.window_handles  #All window capture hobe


for w in all_windows:
   driver.switch_to.window(w) #Ak window theke arek window te jabe


   #Condition diye check kora hocche j new window te gese kina
   if driver.title.__eq__("New Window"):
       new_window_text = driver.find_element(By.XPATH,"//h3").text
       print(new_window_text)
       time.sleep(5)
       driver.close()
       break


driver.switch_to.window(parent_window)
driver.find_element(By.ID,"ta1").send_keys("Rubel Hosain")
time.sleep(5)
driver.close()

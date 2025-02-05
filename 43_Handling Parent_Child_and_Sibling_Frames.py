import time
from selenium import webdriver
from selenium.webdriver.common.by import By

driver = webdriver.Chrome()
driver.maximize_window()
driver.get("https://the-internet.herokuapp.com/nested_frames")
time.sleep(5)

driver.switch_to.frame("frame-top") #Parent1 frame
driver.switch_to.frame("frame-left") #Left child frame
left_child_frame = driver.find_element(By.XPATH,"//body").text
print(left_child_frame)

driver.switch_to.parent_frame() #Child frame back to parent frame
driver.switch_to.frame("frame-middle") #Midle child frame
middle_child_frame = driver.find_element(By.XPATH,"//body").text
print(middle_child_frame)

driver.switch_to.parent_frame() #Child frame back to parent frame
driver.switch_to.frame("frame-right") #Right child frame
right_child_frame = driver.find_element(By.XPATH,"//body").text
print(right_child_frame)

driver.switch_to.default_content() #Child frame back to default frame
driver.switch_to.frame("frame-bottom") #Parent2 frame
bottom_parent_frame = driver.find_element(By.XPATH,"//body").text
print(bottom_parent_frame)
from attr import attributes
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait

driver = webdriver.Chrome()
#Global wait
#driver.implicitly_wait(10)
driver.get("https://omayo.blogspot.com/")
driver.maximize_window()

driver.find_element(By.CLASS_NAME,"dropbtn").click()
#Hard wait
#time.sleep(10)

'''
#Explicit wait system with condition visibility_of_element
wait =  WebDriverWait(driver,30)
gmail_button = wait.until(expected_conditions.visibility_of_element_located((By.LINK_TEXT,"Gmail")))
gmail_button.click()
'''

'''
#Explicit wait system with condition visibility_of_element but located element hidden as a result occurred exception
wait =  WebDriverWait(driver,30)
hide_button = wait.until(expected_conditions.visibility_of_element_located((By.ID,"hbutton")))
hide_button.click()
'''

#Explicit wait system with condition presence_of_element_located it will be handel both visible and hidden element
wait =  WebDriverWait(driver,30)
hide_button = wait.until(expected_conditions.presence_of_element_located((By.ID,"hbutton")))
attribute_name = hide_button.get_attribute("value")
print(attribute_name)







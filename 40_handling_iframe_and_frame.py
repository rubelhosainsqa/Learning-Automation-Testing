import time
from selenium import webdriver
from selenium.webdriver.common.by import By

'''

driver = webdriver.Chrome()
driver.maximize_window()
driver.get("https://the-internet.herokuapp.com/tinymce")
time.sleep(5)

driver.switch_to.frame("tinymce") # Using ID locator for frame, tinymce is value of Frame >> ID
driver.find_element(By.XPATH,"//div[@class='tox-icon']").click()
time.sleep(5)
driver.find_element(By.XPATH,"//body[@id='tinymce']/p").clear()
time.sleep(5)
'''

'''
driver = webdriver.Chrome()
driver.maximize_window()
driver.get("https://docs.oracle.com/javase/8/docs/api/")
time.sleep(5)

driver.switch_to.frame("classFrame")  # Using Name locator for frame, classFrame is value of Frame >> Name

driver.find_element(By.LINK_TEXT,"compact1").click()
time.sleep(5)
'''

driver = webdriver.Chrome()
driver.maximize_window()
driver.get("https://blogpendingtasks.blogspot.com/p/switchtoframeusingwebelement.html")
time.sleep(5)

iframe = driver.find_element(By.XPATH,"//iframe[@title='arunmotoori']")
driver.switch_to.frame(iframe) # Using Xpath locator for frame, iframe is value of Frame >> Xpath

driver.find_element(By.LINK_TEXT,"Home").click()
time.sleep(5)
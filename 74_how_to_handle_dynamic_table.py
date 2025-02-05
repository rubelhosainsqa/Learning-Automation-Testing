import time
from selenium import webdriver
from selenium.webdriver.common.by import By

driver = webdriver.Chrome()
driver.maximize_window()
driver.get("https://demo.opencart.com/admin/index.php?route=common/login")
time.sleep(3)

#driver.find_element(By.ID, "input-username").send_keys("demo")
#driver.find_element(By.ID, "input-password").send_keys("demo")
driver.find_element(By.XPATH,"//button[@type='submit']").click()
time.sleep(10)

driver.find_element(By.XPATH,"//a[contains(text(),'Sales')]").click()

driver.find_element(By.XPATH,"//a[contains(text(),'Orders')]").click()

# driver.find_element(By.XPATH,"//table[@class='table table-bordered table-hover']//tr[3]//td[1]//input").click()

expected_customer_name = "jon snow"
all_customer_name = driver.find_elements(By.XPATH,"//form[@id='form-order']//tr//td[4]")

i = 1
for customer in all_customer_name:
    if customer.text.__eq__(expected_customer_name):
        driver.find_element(By.XPATH,"//form[@id='form-order']//tr["+str(i)+"]//td[1]").click()
    i=i+1

time.sleep(10)
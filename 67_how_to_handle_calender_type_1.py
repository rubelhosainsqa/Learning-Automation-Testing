import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait

driver = webdriver.Chrome()
driver.maximize_window()
driver.get("https://seleniumpractise.blogspot.com/2016/08/how-to-handle-calendar-in-selenium.html")

driver.find_element(By.ID,"datepicker").click()

#Wait for calendar show
wait = WebDriverWait(driver,5)
wait.until(expected_conditions.visibility_of_element_located((By.ID,"ui-datepicker-div")))

#Make a function for reusable code
def select_date_in_calender(month,year,day):

    current_month = driver.find_element(By.CLASS_NAME, "ui-datepicker-month").text
    current_year = driver.find_element(By.CLASS_NAME, "ui-datepicker-year").text

    #Make loop
    while not (current_month.__eq__(month) and current_year.__eq__(year)):
        driver.find_element(By.XPATH, "//span[@class='ui-icon ui-icon-circle-triangle-w']").click()
        current_month = driver.find_element(By.CLASS_NAME, "ui-datepicker-month").text
        current_year = driver.find_element(By.CLASS_NAME, "ui-datepicker-year").text

    driver.find_element(By.XPATH, "//td[@data-handler='selectDay']/a[text()='"+day+"']").click()

#Function call
select_date_in_calender("June","2021","13")

time.sleep(15)










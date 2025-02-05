import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.select import Select
from selenium.webdriver.support.wait import WebDriverWait

driver = webdriver.Chrome()
driver.maximize_window()
driver.get("https://www.hyrtutorials.com/p/calendar-practice.html")
time.sleep(5)

driver.find_element(By.ID,"fourth_date_picker").click()

#Wait for calendar show
wait = WebDriverWait(driver,5)
wait.until(expected_conditions.visibility_of_element_located((By.ID,"ui-datepicker-div")))

month = driver.find_element(By.CLASS_NAME,"ui-datepicker-month")
month_dropdown = Select(month)
month_dropdown.select_by_visible_text("Apr")

year = driver.find_element(By.CLASS_NAME,"ui-datepicker-year")
year_dropdown = Select(year)
year_dropdown.select_by_visible_text("2025")

driver.find_element(By.XPATH,"//td[not(contains(@class,'ui-datepicker-week-end ui-datepicker-other-month'))]/a[text()='26']").click()
time.sleep(5)




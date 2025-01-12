import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select # This is used for select dropdown

driver = webdriver.Chrome()
driver.maximize_window()
driver.get("https://omayo.blogspot.com/")
time.sleep(5)

dropdown = driver.find_element(By.ID,"drop1")

select = Select(dropdown)
# select.select_by_visible_text("doc 1")  # select_by_visible_text is used for select a  value from dropdown list by visible text
# select.select_by_index(4)  # select_by_index is used for select a value from dropdown list by index number
select.select_by_value("def") # select_by_value is used for select a value from dropdown list by value
time.sleep(5)

if select.is_multiple: #is_multiple is used for know is that dropdown list or multiple selected list
    print("This is multiple select")
else:
    print("This is dropdown list")

dropdown_option = select.options  # options is used for print all dropdown list
for a in dropdown_option:
    print(a.text)

b = select.first_selected_option # first_selected_option is used for print the first option from the dropdown list
print(b.text)
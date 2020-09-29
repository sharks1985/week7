# Project 1: Creating an account in automationpractice.com

# - Sign In> enter email> click on Create Account > Fill the forms
# - finding all elements (xpath, id, name)
# - verify that account is created by message, logout button

from steps.webdriver_functions import *
from selenium.webdriver.support.select import Select0

sign_in_link = "//a[@class='login']"
email_input_xpath = "//input[@id='email_create']"
email = "tatianashark777@email.com"
create_an_account_button = "//form[@id='create-account_form']//span[1]"
title_input = "//input[@id='id_gender2']"
first_name_input_xpath = "//input[@id='customer_firstname']"
first_name = "Tatiana"
last_name_input_xpath = "//input[@id='customer_lastname']"
last_name = "Shark"
password_input_xpath = "//input[@id='passwd']"
password = "928Hello!!!"
dob_date_input_xpath = "//select[@id='days']"
dob_month_input_select_xpath = "//option[contains(text(),'January')]"
dob_year_input_xpath = "//select[@id='years']"
special_offers_cell_xpath = "//input[@id='optin']"
address_input_xpath = "//input[@id='address1']"
city_input_xpath = "//input[@id='city']"
state_input_xpath = "//select[@id='id_state']"
zip_code_input_xpath = "//input[@id='postcode']"
mob_phone_input_xpath = "//input[@id='phone_mobile']"
assign_the_address_alias_input_xpath = "//input[@id='alias']"
register_button = "//span[contains(text(),'Register')]"
sign_out_link = "//a[@class='logout']"

launch_website("http://automationpractice.com/index.php")
click_element_by_xpath(sign_in_link)
time.sleep(2)
enter_text_by_xpath(email_input_xpath, email)
time.sleep(2)
click_element_by_xpath(create_an_account_button)
time.sleep(2)
click_element_by_xpath(title_input)
time.sleep(2)
enter_text_by_xpath(first_name_input_xpath, first_name)
time.sleep(2)
enter_text_by_xpath(last_name_input_xpath, last_name)
time.sleep(2)
enter_text_by_xpath(password_input_xpath, password)
time.sleep(2)
enter_text_by_xpath(dob_date_input_xpath, 19)
time.sleep(2)
click_element_by_xpath(dob_month_input_select_xpath)
time.sleep(2)
enter_text_by_xpath(dob_year_input_xpath, '2000')
time.sleep(2)
click_element_by_xpath(special_offers_cell_xpath)
time.sleep(2)
enter_text_by_xpath(address_input_xpath, '777 Lucky Street')
time.sleep(2)
enter_text_by_xpath(city_input_xpath, 'Joy')
time.sleep(2)
enter_text_by_xpath(state_input_xpath, 'New York')
time.sleep(2)
enter_text_by_xpath(zip_code_input_xpath, '11229')
time.sleep(2)
enter_text_by_xpath(mob_phone_input_xpath, '7188371888')
time.sleep(2)
enter_text_by_xpath(assign_the_address_alias_input_xpath, 'My address')
time.sleep(2)
click_element_by_xpath(register_button)


time.sleep(2)

heading_xpath = "//span[contains(text(),'Tatiana Shark')]"
element = driver.find_element_by_xpath(heading_xpath)
assert 'Tatiana Shark' in element.text
print("Congrats! Your account is successfully created.")

click_element_by_xpath(sign_out_link)
print("Logging out now")


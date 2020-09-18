from selenium.webdriver import ActionChains
from selenium.webdriver.common.keys import Keys

from webdriver_class.webdriver_functions import *

# # ********* Scenario with correct steps
# launch_website("https://letskodeit.teachable.com/p/practice")
# find_elements_tag('button')
# web_driver_properties_switch_to_tab()
# close_browser()

# # ********* Scenario for go back, forward, refresh
# launch_website("http://automationpractice.com/index.php")
# women_tab = "//a[@class='sf-with-ul'][contains(text(),'Women')]"
# click_element_by_xpath(women_tab)
# go_back_to_previous_page()
# refresh_browser()
# go_next_page()
# close_browser()

# # *********** Scenario: Login to "http://automationpractice.com/index.php"
# Prerequisite: create an account:
# username: hello@email.com, have strong password: "$Password001"
# identify all locators by inspecting on browser (xpath, optional: id, css selector):
# sign_in_link = "//a[@class='login']"
# #
# # # sign_in_link = "//a[@class='login'" # this is incorrect XPATH, to see Try Except
# # email_input = "//input[@id='email']"
# # password_input = "//input[@id='passwd']"
# # sign_in_button = "//button[@id='SubmitLogin']"
# # sign_out_link = "//a[@class='logout']"
# #
# # # Steps:
# # launch_website("http://automationpractice.com/index.php")
# # click_element_by_xpath(sign_in_link)
# # time.sleep(2)
# # enter_text_by_xpath(email_input, "hello@email.com")
# # enter_text_by_xpath(password_input, "$Password001")
# # click_element_by_xpath(sign_in_button)
# # time.sleep(10)
# # print("successfully signed in ")
# # print("signing out now...")
# # click_element_by_xpath(sign_out_link)
# # close_browser()

# newid = driver.find_element_by_xpath('').get_attribute('id')
    # dynamic_xpath = "//span[@id=obj123456]"
    # dynamic_xpath = f"//span[@id=obj1{newid}]"
    # dynamic_xpath = "//span[contains(@id, 'j1')]"
    # dynamic_xpath = "//span[ends-with(@id, '56')]"
    # dynamic_xpath = "//span[starts-with(@id, 'obj')]"
    # import re
    #
    # def get_xpath(id_num):
    #     return "//span[@id='" + id_num + "']"
    #

# H/W : Sign In> enter email> click on Create Account > Fill the forms
# finding all elements (xpath, id, name)

# Scenario: Right click
# TODO: find out right way to retrieve chrome right click options, which is not Element property
# Steps:
# sign_in_link = "//a[@class='login']"
# launch_website("http://automationpractice.com/index.php")
# sign_in_element = driver.find_element_by_xpath(sign_in_link)
# actions = ActionChains(driver)
# actions.context_click(sign_in_element).send_keys(Keys.ARROW_DOWN).send_keys(Keys.ARROW_DOWN).build().perform()
# actions.send_keys(Keys.ARROW_DOWN).perform()
# actions.send_keys(Keys.ENTER).perform()

# Scenario: Drag and Drop
# # locators:
# item1_xpath = "//div[@id='todrag']//span[contains(text(),'Draggable 1')]"
# item2_xpath = "//div[@id='todrag']//span[contains(text(),'Draggable 2')]"
# drop_zone_xpath = "//div[@id='mydropzone']"
# dropped_item1_xpath = "//div[@id='droppedlist']//span[contains(text(),'Draggable 1')]"
# dropped_item2_xpath = "//div[@id='droppedlist']//span[contains(text(),'Draggable 2')]"
#
# # Step:
# # start the website
# # drag and drop item 1
# # verify item 1 is under dropped list
# # drag and drop item 2
# # verify item 2 is under dropped list
#
# # launch_website("https://www.seleniumeasy.com/test/drag-and-drop-demo.html")
# # launch_website("https://artoftesting.com/samplesiteforselenium")
# launch_website("http://testautomationpractice.blogspot.com/")
# item1 = driver.find_element_by_xpath("//div[@id='draggable']")
# drop_zone = driver.find_element_by_xpath("//div[@id='droppable']")
# #
# actions = ActionChains(driver)
# actions.drag_and_drop(item1, drop_zone).perform()
# # actions.move_to_element(item1, drop_zone).perform() # hover over element (mouse movement)
# print("drag and drop finished.")


# Scenario: is_displayed(), is_selected(), is_enabled()

launch_website("https://letskodeit.teachable.com/p/practice")

xpath1 = "//div[@id='radio-btn-example']"
radio_button_example = driver.find_element_by_xpath(xpath1)
print(f"Radio button example is displayed: {radio_button_example.is_displayed()}")

if radio_button_example.is_displayed():
    bmw_option = driver.find_element_by_xpath("//input[@id='bmwradio']")
    bmw_option.click()
    time.sleep(1)
else:
    print("Radio button example is not displayed")

print('bwm option is clicked')
print(f"Is bmw option selected: {bmw_option.is_selected()}")
assert bmw_option.is_selected(), "bmw Option is not selected "
print("Yeaah it is selected. Test Passed")

print("getting the attribute of the element")
button = driver.find_element_by_xpath("//button[@id='openwindow']")
value1 = button.get_attribute("onclick")
value2 = button.get_attribute("class")
print(f"Attributes of the element: onlick: {value1} , class: {value2}")
print(f"Text of the button : {button.text}")


# agenda for next class:
# drop down list
# alert (confirm, cancel) - java script
#  explicit waits , and difference between implicit_wait()
# hover over element
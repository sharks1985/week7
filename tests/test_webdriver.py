from webdriver_class.webdriver_functions import *

#  Scenario with correct steps
# launch_website("https://letskodeit.teachable.com/p/practice")
# find_elements_tag('button')
# web_driver_properties_switch_to_tab()
# close_browser()

launch_website("http://automationpractice.com/index.php")
women_tab = "//a[@class='sf-with-ul'][contains(text(),'Women')]"
click_element_by_xpath(women_tab)
go_back_to_previous_page()
refresh_browser()
go_next_page()
close_browser()


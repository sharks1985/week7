
# week8 09/19/2020,
# Class project1: Creating an account in automationpractice.com
# H/W :
# Sign In> enter email> click on Create Account > Fill the forms
# finding all elements (xpath, id, name)
# verify that account is created by message, logout button


#  Class project: hard project
# uploading a file
# open browser, launch the "https://www.facebook.com/marketplace",
# login to facebook
# create new listing, choose item for sale, verify the url: "https://www.facebook.com/marketplace/create/item"
upload_xpath = "//input[@type='file' and contains(@accept, 'image')]"
price_input = "//label[@aria-label='Price']//input[contains(@id, 'jsc_c_')]"
title_input = "//label[@aria-label='Title']//input[contains(@id, 'jsc_c_')]"
category_list = "//label[@aria-label='Category']//span"
category_item = "//span[contains(text(),'Electronics')]"
category_sub_item = "//span[contains(text(),'Blank Media')]"
condition_list = "//span[contains(text(),'Condition')]"
condition_option = "//div[contains(text(),'Used - Like New')]"
next_button_xpath = "//div[@aria-label='Next']"
title = 'Iphone25'

# image_path = "C:\\Users\\akhus\Desktop\\thinkorswim-simulated-trading.png"
image_path = "C:/Users/akhus/Desktop/thinkorswim-simulated-trading.png"
image_upload = driver.find_element_by_xpath(upload_xpath)
image_upload.send_keys(image_path)

# to check next button is enabled:
next_button = driver.find_element_by_xpath(next_button_xpath)
if next_button.is_enabled():
    next_button.click()
    print("Next button is clicked.")


# after listing is published verify url= "https://www.facebook.com/marketplace/you/selling"
# verify the item is listed
active_item1_xpath = f"//span[contains(text(), '{title}')]"
active_item1 = driver.find_element_by_xpath(active_item1_xpath)
time.sleep(5)
assert active_item1.is_displayed()
print("Test is successfully executed!!")

# Commit , push to github, and submit with google form (akmal to send this form in the chat)

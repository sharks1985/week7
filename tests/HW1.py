## Project 1: Creating an account in automationpractice.com

# - Sign In> enter email> click on Create Account > Fill the forms
# - finding all elements (xpath, id, name)
# - verify that account is created by message, logout button
import time
import selenium
from selenium import webdriver
from selenium.webdriver import ActionChains
from selenium.webdriver.common.keys import Keys
from steps.webdriver_functions import *
from steps.webelement_functions import *

# launch_website("http://automationpractice.com/index.php")
driver = webdriver.Chrome()


def launch_website():
    driver.get("http://automationpractice.com/index.php")

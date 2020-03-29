import os
from selenium import webdriver

browser = webdriver.Firefox()
browser.get('https://reddit.com/')
searchelem = browser.find_element_by_css_selector(".search-field")
searchelem.send_keys('How to print hello world')
searchelem.submit()

os.system("pause")
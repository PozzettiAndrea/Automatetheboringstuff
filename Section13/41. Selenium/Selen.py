import os
from selenium import webdriver

browser = webdriver.Firefox()
browser.get('https://automatetheboringstuff.com')
#elem = browser.find_element_by_css_selector("body > div.main > div:nth-child(1) > ul:nth-child(20) > li:nth-child(14)")
#print(elem)
#elem.click()
elems = browser.find_elements_by_css_selector("p")
print(len(elems))

os.system("pause")
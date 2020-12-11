import selenium
from selenium import webdriver

print("here we go")
driver = webdriver.Chrome()

driver.switch_to.new_window('tab')

driver.get("http://www.python.org")

print('and we are done')

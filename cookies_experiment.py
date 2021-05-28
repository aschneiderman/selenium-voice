from selenium import webdriver
driver=webdriver.Chrome()
driver.get("https://trello.com/")

import time
time.sleep(1)

cookies = driver.get_cookies()
print(cookies)

# https://stackoverflow.com/questions/63106821/problem-loading-cookies-with-selenium-and-python
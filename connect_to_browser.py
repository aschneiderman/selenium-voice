# chrome.exe -remote-debugging-port=9222
# cd "C:\Program Files (x86)\Google\Chrome\Application"
# chrome.exe -remote-debugging-port=9014 --user-data-dir="%LOCALAPPDATA%\Google\Chrome\User Data"

import selenium
from selenium import webdriver

from selenium.webdriver.chrome.options import Options

chrome_options = Options()
chrome_options.add_experimental_option("debuggerAddress", "localhost:9014")
driver = webdriver.Chrome(options=chrome_options)
# driver = webdriver.Chrome()

print "here we go"
driver.get("https://www.python.org/")

# print "here we go"

driver.get("https://trello.com/b/jbIYuZmS/anders-client-test")

# driver.get("https://www.nytimes.com/")
# # driver.get("https://www.google.com/")


 

# https://stackoverflow.com/questions/51214668/python-selenium-how-to-use-debugger-address-option-in-chrome-driver-for-remote
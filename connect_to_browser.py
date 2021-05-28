# This script relies on connecting to a version of Google Chrome that is in remote debugging mode.
# NOTE: this will start up Google, using your current user profile, so all of your cookies & logins willl work
# You can use whatever port you want; just change the script below
#
# To get it up and running, run the following 2 commands from the command prompt (clicck on the search box, type "cmd")
# cd "C:\Program Files (x86)\Google\Chrome\Application"
# chrome.exe -remote-debugging-port=9014 --user-data-dir="%LOCALAPPDATA%\Google\Chrome\User Data"

import selenium
from selenium import webdriver
from selenium.webdriver.chrome.options import Options

chrome_options = Options()
chrome_options.add_experimental_option("debuggerAddress", "localhost:9014")
driver = webdriver.Chrome(options=chrome_options)

print "here we go"

driver.get("https://trello.com/b/jbIYuZmS/anders-client-test")



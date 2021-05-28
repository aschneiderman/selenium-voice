import selenium
from selenium import webdriver

from selenium.webdriver.chrome.options import Options
chrome_options = Options() 
chrome_options.add_experimental_option("detach", True)

driver = webdriver.Chrome('chromedriver.exe', chrome_options=chrome_options, options=chrome_options)
# drivers = webdriver.Chrome()
driver.get("https://www.python.org/")
import time

print "here we go"

driver.get("https://trello.com/")

driver.get("https://www.nytimes.com/")
driver.get("https://www.google.com/")


 
time.sleep(1)
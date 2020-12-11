import selenium
from selenium import webdriver
from selenium.webdriver.common.keys import Keys

driver = webdriver.Chrome()
driver.get("http://www.python.org")
assert "Python" in driver.title
elem = driver.find_element_by_name("q")
elem.clear()
elem.send_keys("pycon")
elem.send_keys(Keys.RETURN)
assert "No results found." not in driver.page_source
driver.close()

"""
https://selenium-python.readthedocs.io/index.html

The problem:
C:\Program Files\Python39>pip install selenium
Requirement already satisfied: selenium in c:\python27\lib\site-packages (3.141.0)
Requirement already satisfied: urllib3 in c:\python27\lib\site-packages (from selenium) (1.25.9)
You are using pip version 18.1, however version 20.3.1 is available.
You should consider upgrading via the 'python -m pip install --upgrade pip' command.

C:\Program Files\Python39> c: && cd c:\Users\aschn\Documents\GitHub\selenium-voice && cmd /C ""C:\Program Files\Python39\python.exe" c:\Users\aschn\.vscode\extensions\ms-python.python-2020.11.371526539\pythonFiles\lib\python\debugpy\launcher 50527 -- c:\Users\aschn\Documents\GitHub\selenium-voice\test_selenium.py "

So how do I get to decide which version of Python it's using?

For that matter, which version does Castor use?

"""
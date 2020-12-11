import selenium
from selenium import webdriver
from selenium.webdriver.common.keys import Keys

print("here we go")
driver = webdriver.Chrome()
driver.get("http://www.python.org")
assert "Python" in driver.title
elem = driver.find_element_by_name("q")
elem.clear()
elem.send_keys("pycon")
elem.send_keys(Keys.RETURN)
assert "No results found." not in driver.page_source
# driver.close()

print('and we are done')


"""
NOTES:

Test_dragonfly seems to be using the approach outlined in this article:
https://cosmocode.io/how-to-connect-selenium-to-an-existing-browser-that-was-opened-manually/

---------------------------------------------------------------------------------------
from selenium import webdriver

driver = webdriver.Chrome()
executor_url = driver.command_executor._url
session_id = driver.session_id
driver.get("http://tarunlalwani.com")

print session_id
print executor_url


driver2 = webdriver.Remote(command_executor=executor_url, desired_capabilities={})
driver2.session_id = session_id
print driver2.current_url
When we run the above code, it prints the url http://tarunlalwani.com at the end. Which means we were able to recreate the driver object for a Chrome browser.

---------------------------------------------------------------------------------------

To open a browser and keep it open:

If you want chrome and chromedriver to stay open, you have to use the 'detach' option when starting chromedriver.

In your case add :

from selenium.webdriver.chrome.options import Options
chrome_options = Options()
chrome_options.add_experimental_option("detach", True)
Or you can run the code in debug mode with breakpoint at the end and when it pauses 'kill' the program and take over the browser if you want to, but this works in IDE only.

Is it possible to reuse this browser window? E.g. get the PID or something and use explicitly if exists? 

With Python you use chrome_options.add_experimental_option("detach", True), with C# you use the ChromeOptions.LeaveBrowserOpen property... either way tho neither of them will function until you add options.AddExcludedArgument("enable-automation") to your options setup




If you want to leave the browser open until you manually close it, you will need to enable chrome options when you create your webdriver.

from selenium.webdriver.chrome.options import Options

chrome_options = Options() chrome_options.add_experimental_option("detach", True)

driver = webdriver.Chrome(options=chrome_options)

Hopefully all of the syntax is right, I did this on mobile. If it's wrong, this should give you enough to effectively Google the solution.



options = webdriver.ChromeOptions()
options.add_experimental_option("detach", True)
driver = webdriver.Chrome(chrome_options=options, executable_path=r'C:\WebDrivers\chromedriver.exe')




"""
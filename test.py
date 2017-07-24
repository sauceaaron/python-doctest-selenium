import os
import sys
from selenium import webdriver
from sauceclient import SauceClient

from page import SandboxPage

username = os.environ.get("SAUCE_USERNAME")
access_key = os.environ.get("SAUCE_ACCESS_KEY")

command_executor = "http://%s:%s@ondemand.saucelabs.com:80/wd/hub" % (username, access_key)

desired_capabilities = {
	"platform": os.environ.get("platform"),
	"browserName": os.environ.get("browserName"),
	"version": os.environ.get("version")
}

driver = webdriver.Remote(
	command_executor=command_executor, 
	desired_capabilities= desired_capabilities
)

def check_title(sandbox):
	"""
		It should have the correct title

		>>> check_title(driver)
		False
	"""	

	sandbox = SandboxPage(driver)
	sandbox.open()
	return sandbox.title == driver.title


if __name__ == '__main__':
	try: 

	    import doctest
	    doctest.testmod()
	finally:
		driver.quit()

		sauce_client = SauceClient(username, access_key)
		status = (sys.exc_info() == (None, None, None))
		sauce_client.jobs.update_job(driver.session_id, passed=status)


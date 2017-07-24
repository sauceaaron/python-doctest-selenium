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

# url = "http://saucelabs.github.io/training-test-page/"

try: 
	sandbox = SandboxPage(driver)
	sandbox.open()
	assert driver.title == "I am a page title - Sauce Labs"

finally:
	driver.quit()

	sauce_client = SauceClient(username, access_key)
	status = (sys.exc_info() == (None, None, None))
	sauce_client.jobs.update_job(driver.session_id, passed=status)
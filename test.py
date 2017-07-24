import os
import sys
from selenium import webdriver
from sauceclient import SauceClient

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

url = "http://saucelabs.github.io/training-test-page/"

driver.get(url)
driver.quit()
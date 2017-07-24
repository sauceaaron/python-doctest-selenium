class SandboxPage:

	url = "http://saucelabs.github.io/training-test-page/"
	title = "I am a page title - Sauce Labs"

		def __init__(self, driver):
			self.driver = driver
	
		def open(self):
			self.driver.get(self.url)
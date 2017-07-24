class SandboxPage:

		def __init__(self, driver):
			self.driver = driver
			self.url = "http://saucelabs.github.io/training-test-page/"

		def open(self):
			self.driver.get(self.url)
import unittest

from selenium import webdriver
from ddt import ddt, data, unpack
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions
import time

@ddt
class testddt(unittest.TestCase):

	@classmethod
	def setUpClass(cls):

		cls.driver = webdriver.Chrome("C:\Personal\Development\Python\seliniumtest\chromedriver.exe")
		cls.driver.implicitly_wait(10)
		cls.driver.maximize_window()

		cls.driver.get("http://www.google.co.in")

	@data(("horns",9),("Food", 10))
	@unpack
	def test001_ddt(self, item_name , item_count ):

		driver = self.driver
		print (driver.title)

		search = driver.find_element_by_name("q")
		search.clear()
		search.send_keys(item_name)
		#WebDriverWait(driver, 10).until(lambda s:s.find_element_by_name("q").text == item_name)
		search.submit()
		time.sleep(2)
		links = driver.find_elements_by_class_name("r")

		self.assertEqual(item_count , len(links))


if __name__ == "__main__":
	unittest.main(verbosity=2)


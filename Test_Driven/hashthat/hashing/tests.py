from django.test import TestCase

from selenium import webdriver

class FunctionaTestCase(TestCase):
    def setUp(self):
        self.browser=webdriver.Firefox()

    def test_there_is_homepage(self):
        self.browser.get('http://localhost:8000')
        self.assertIn('Enter hash here:',self.browser.page_source)

    def test_hash_to_hello(self):
        self.browser.get('http://localhost:8000')
        text=self.browser.find_element_by_id('id_text')
        text.send_keys('hello')
        self.browser.find_element_by_name('submit').click()
        self.assertIn('2cf2dba5fb0a30e26e83b2ac5b9e29e1b161e5c1fa7425e73043362938b9824', self.browser.page_source)

    def tearDown(self):
        self.browser.quit()

class UnitTestCase(TestCase):
    
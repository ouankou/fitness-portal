import unittest
from django.test import TestCase,Client
from django.urls import reverse
from selenium import webdriver
import time

class TestUIworkflow(unittest.TestCase):

    def test_upper(self):
        print("here1")
        self.assertEqual('foo'.upper(), 'FOO')

    def test_login_UI(self):
        driver = webdriver.Chrome("/Library/Frameworks/Python.framework/Versions/3.7/bin/chromedriver");
        driver.get("http://localhost:8000/")
        time.sleep(1)
        driver.find_element_by_id("login-dropdown").click()
        time.sleep(1)
        driver.find_element_by_id("exampleInputEmail2").send_keys("testuser")
        time.sleep(1)
        driver.find_element_by_id("exampleInputPassword2").send_keys("testpassword")
        time.sleep(1)
        driver.find_element_by_id("sign-in").click()
        driver.close()

    def test_login_UI_new(self):
        driver = webdriver.Chrome("/Library/Frameworks/Python.framework/Versions/3.7/bin/chromedriver");
        driver.get("http://localhost:8000/")
        time.sleep(1)
        driver.find_element_by_id("login-dropdown").click()
        time.sleep(1)
        driver.find_element_by_id("exampleInputEmail2").send_keys("testuser")
        time.sleep(1)
        driver.find_element_by_id("exampleInputPassword2").send_keys("testpassword")
        time.sleep(1)
        driver.find_element_by_id("sign-in").click()
        driver.close()

if __name__ == '__main__':
    unittest.main()
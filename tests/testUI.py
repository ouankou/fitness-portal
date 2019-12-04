import unittest
from django.test import TestCase,Client
from django.urls import reverse
from selenium import webdriver
from selenium.webdriver.support.ui import Select
import time
import random

class TestUIworkflow(unittest.TestCase):


#####test to check whether application home page is launnching succesfully or not  ####

    def test_homepage(self):
        driver = webdriver.Chrome("/Library/Frameworks/Python.framework/Versions/3.7/bin/chromedriver");
        wait()
        driver.get("http://localhost:8000/")
        wait()
        homepagetext = driver.find_element_by_class_name("cover-heading")
        self.assertEqual(homepagetext.text, "Start today!")
        driver.close()




#######test to check if trainer is successfully able to login to the application####

    def test_trainer_login(self):

        driver = webdriver.Chrome("/Library/Frameworks/Python.framework/Versions/3.7/bin/chromedriver");
        wait()
        driver.get("http://localhost:8000/")
        wait()
        driver.find_element_by_id("login-dropdown").click()
        wait()
        driver.find_element_by_id("exampleInputEmail2").send_keys("trainer")
        wait()
        driver.find_element_by_id("exampleInputPassword2").send_keys("1234")
        wait()
        driver.find_element_by_id("sign-in").click()
        wait()
        login_text=driver.find_elements_by_class_name("nav-link")[0]
        self.assertEqual(login_text.text, "Welcome to Trainer Portal")
        driver.close()

####### test to check if logout button button functionalty is working for trainer ####
    def test_trainer_logout(self):
        driver = webdriver.Chrome("/Library/Frameworks/Python.framework/Versions/3.7/bin/chromedriver");
        wait()
        driver.get("http://localhost:8000/")
        wait()
        driver.find_element_by_id("login-dropdown").click()
        wait()
        driver.find_element_by_id("exampleInputEmail2").send_keys("trainer")
        wait()
        driver.find_element_by_id("exampleInputPassword2").send_keys("1234")
        wait()
        driver.find_element_by_id("sign-in").click()
        wait();wait()
        logout_button=driver.find_elements_by_class_name("nav-link")[1]
        self.assertEqual(logout_button.text,"Logout")
        logout_button.click()
        homepagetext=driver.find_element_by_class_name("cover-heading")
        self.assertEqual(homepagetext.text, "Start today!")
        driver.close()



######test to check if client is successfully able to login to the application########
    def test_client_login(self):
        driver = webdriver.Chrome("/Library/Frameworks/Python.framework/Versions/3.7/bin/chromedriver");
        driver.get("http://localhost:8000/")
        time.sleep(1)
        driver.find_element_by_id("login-dropdown").click()
        time.sleep(1)
        driver.find_element_by_id("exampleInputEmail2").send_keys("test123new")
        time.sleep(1)
        driver.find_element_by_id("exampleInputPassword2").send_keys("1234")
        time.sleep(1)
        driver.find_element_by_id("sign-in").click()
        driver.close()

#######test to check if admin is successfully able to login and logout from the application####

    def test_admin_login(self):

        driver = webdriver.Chrome("/Library/Frameworks/Python.framework/Versions/3.7/bin/chromedriver");
        wait()
        driver.get("http://localhost:8000/")
        wait()
        driver.find_element_by_id("login-dropdown").click()
        wait()
        driver.find_element_by_id("exampleInputEmail2").send_keys("admin")
        wait()
        driver.find_element_by_id("exampleInputPassword2").send_keys("admin")
        wait()
        driver.find_element_by_id("sign-in").click()
        wait()
        login_text=driver.find_elements_by_class_name("nav-link")[0]
        self.assertEqual(login_text.text, "Welcome to Admin Portal")
        wait()
        login_text = driver.find_elements_by_class_name("display-4")[0]
        self.assertEqual(login_text.text, "Pending applications")
        logout_button = driver.find_elements_by_class_name("nav-link")[1]
        self.assertEqual(logout_button.text, "Logout")
        logout_button.click()
        homepagetext = driver.find_element_by_class_name("cover-heading")
        self.assertEqual(homepagetext.text, "Start today!")
        driver.close()


    ###test to check the trainer signup form ########
    def test_trainer_singup(self):
        suffix=random.randint(1,1000)
        driver = webdriver.Chrome("/Library/Frameworks/Python.framework/Versions/3.7/bin/chromedriver");
        wait()
        driver.get("http://localhost:8000/")
        wait()
        trainer_button=driver.find_elements_by_class_name("btn-secondary")[0]
        self.assertEqual(trainer_button.text, "Trainer")
        trainer_button.click()
        application_form= driver.find_elements_by_class_name("display-4")[0]
        self.assertEqual(application_form.text, "Trainer Application Form")
        driver.find_element_by_id("first_name").send_keys("testuser")
        driver.find_element_by_id("last_name").send_keys("test")
        wait()

        driver.find_element_by_id("username").send_keys("user123"+str(suffix))
        driver.find_element_by_id("password").send_keys("test")

        wait()
        driver.find_element_by_id("password-confirmation").send_keys("test")

        driver.find_element_by_id("email").send_keys("testuser"+str(suffix)+"@test.com")
        driver.find_element_by_id("years_of_experience").send_keys("2")
        driver.find_element_by_id("charge").send_keys("20")
        wait()
        select = Select(driver.find_element_by_id('location_served'))
        select.select_by_index(1)
        wait()
        driver.find_element_by_id("nasm").click()
        wait()
        driver.find_elements_by_class_name("btn-primary")[1].click()
        wait()
        application_review_text=driver.find_element_by_class_name("alert-info")
        self.assertEqual(application_review_text.text, "Your application is under review. We will get back to you shortly!")
        driver.close()




 

def wait():
    time.sleep(2)

if __name__ == '__main__':
    unittest.main()
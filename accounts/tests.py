from django.test import LiveServerTestCase
from django.urls import reverse_lazy
from selenium import webdriver
from selenium.webdriver.common.by import By
import time
# Create your tests here.
class TestLogin(LiveServerTestCase):
    @classmethod
    def setUpClass(cls):
        super().setUpClass()
        cls.selenium = webdriver.Chrome()
        
    @classmethod
    def tearDownClass(cls):
        cls.selenium.quit()
        super().tearDownClass()
    
    def test_login(self):
        self.selenium.get('http://localhost:8000'+str(reverse_lazy(('account_login'))))
        
        username_input = self.selenium.find_element(By.NAME,"login")
        username_input.send_keys('testuser@gmail.com')
        
        password_input = self.selenium.find_element(By.NAME,"password")
        password_input.send_keys('test0000')
        
        button = self.selenium.find_element(By.XPATH,'//*[@id="wrapper]/div/div/form/button')
        button.click()
        
        time.sleep(3)
        self.assertEqual('日記一覧 | Private Diary',self.selenium.title)
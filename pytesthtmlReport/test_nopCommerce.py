from selenium import webdriver
import pytest
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By

class Test_nopCom():
    @pytest.fixture()
    def setup(self):
        serv_object = Service("C://Users//Reka//Drivers//chromedriver.exe")
        self.driver= webdriver.Chrome(service=serv_object)
#       driver=webdriver.Chrome()
        self.driver.maximize_window()
        yield
        self.driver.close()

    def test_homepagetitle(self,setup):
        self.driver.get("https://admin-demo.nopcommerce.com/")
        assert self.driver.title=="Your store. Login",self.driver.title

    def test_login(self,setup):
        self.driver.get("https://admin-demo.nopcommerce.com/")
        self.driver.find_element(By.XPATH,"//*[@id='Email']").clear()
        self.driver.find_element(By.XPATH,"//*[@id='Email']").send_keys("admin@yourstore.com")
        self.driver.find_element(By.XPATH,"//*[@id='Password']").clear()
        self.driver.find_element(By.XPATH,"//*[@id='Password']").send_keys("admin")
        self.driver.find_element(By.XPATH,"//button[normalize-space()='Log in']").click()
        assert self.driver.title=="Dashboard / nopCommerce administration"

#   pytest -v -s C:\Users\Reka\PycharmProject\pytestHTMLreport\pytesthtmlReport\test_nopCommerce.py
# OR
#   pytest -v -s pytesthtmlReport/test_nopCommerce.py

#Report Generation
#   pytest -v -s --html=Report.html pytesthtmlReport/test_nopCommerce.py
# OR
#   pytest -v -s --html=Report.html --self-contained-html pytesthtmlReport/test_nopCommerce.py
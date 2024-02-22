from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
import unittest


class TestCustomerForm(unittest.TestCase):

    def setUp(self):
        # Initialize the Chrome WebDriver with ChromeOptions
        options = webdriver.ChromeOptions()
        options.add_experimental_option('excludeSwitches', ['enable-logging'])
        s = Service('D:\webdriver\chromedriver.exe')
        self.driver = webdriver.Chrome(service=s, options=options)

    def tearDown(self):
        self.driver.quit()

    def test_customer_form_01(self):
        self.driver.get("http://localhost/web/index.html")

        firstname_input = self.driver.find_element(By.ID, "firstname")
        lastname_input = self.driver.find_element(By.ID, "lastname")
        age_input = self.driver.find_element(By.ID, "age")
        
        firstname_input.send_keys("JohnJohn")
        lastname_input.send_keys("canonc")
        age_input.send_keys("2")

        submit_button = self.driver.find_element(By.TAG_NAME, "button")
        submit_button.click()

        result = self.driver.find_element(By.ID, "firstname").text

        print(self.driver.title)

        self.assertEqual("First Name: JohnJohn", result)
        self.driver.save_screenshot("img/test_customer_form_01.png")

    def test_customer_form_02(self):
        self.driver.get("http://localhost/web/index.html")

        firstname_input = self.driver.find_element(By.ID, "firstname")
        lastname_input = self.driver.find_element(By.ID, "lastname")
        age_input = self.driver.find_element(By.ID, "age")
        
        firstname_input.send_keys("Johnj")
        lastname_input.send_keys("canoncanoncano")
        age_input.send_keys("149")

        submit_button = self.driver.find_element(By.TAG_NAME, "button")
        submit_button.click()

        result = self.driver.find_element(By.ID, "firstname").text

        print(self.driver.title)

        self.assertEqual("First Name: Johnj", result)
        self.driver.save_screenshot("img/test_customer_form_02.png")

    def test_customer_form_03(self):
        self.driver.get("http://localhost/web/index.html")

        firstname_input = self.driver.find_element(By.ID, "firstname")
        lastname_input = self.driver.find_element(By.ID, "lastname")
        age_input = self.driver.find_element(By.ID, "age")
        
        firstname_input.send_keys("Johnjo")
        lastname_input.send_keys("canoncanoncanon")
        age_input.send_keys("150")

        submit_button = self.driver.find_element(By.TAG_NAME, "button")
        submit_button.click()

        result = self.driver.find_element(By.ID, "firstname").text

        print(self.driver.title)

        self.assertEqual("First Name: Johnjo", result)
        self.driver.save_screenshot("img/test_customer_form_03.png")

    def test_customer_form_04(self):
        self.driver.get("http://localhost/web/index.html")

        firstname_input = self.driver.find_element(By.ID, "firstname")
        lastname_input = self.driver.find_element(By.ID, "lastname")
        age_input = self.driver.find_element(By.ID, "age")
        
        firstname_input.send_keys("Johnjohnjohnjo")
        lastname_input.send_keys("canoncan")
        age_input.send_keys("75")

        submit_button = self.driver.find_element(By.TAG_NAME, "button")
        submit_button.click()

        result = self.driver.find_element(By.ID, "firstname").text

        print(self.driver.title)

        self.assertEqual("First Name: Johnjohnjohnjo", result)
        self.driver.save_screenshot("img/test_customer_form_04.png")

    def test_customer_form_05(self):
        self.driver.get("http://localhost/web/index.html")

        firstname_input = self.driver.find_element(By.ID, "firstname")
        lastname_input = self.driver.find_element(By.ID, "lastname")
        age_input = self.driver.find_element(By.ID, "age")
        
        firstname_input.send_keys("Johnjohnjohnjoh")
        lastname_input.send_keys("canoncan")
        age_input.send_keys("75")

        submit_button = self.driver.find_element(By.TAG_NAME, "button")
        submit_button.click()

        result = self.driver.find_element(By.ID, "firstname").text

        print(self.driver.title)

        self.assertEqual("First Name: Johnjohnjohnjoh", result)
        self.driver.save_screenshot("img/test_customer_form_05.png")

    def test_customer_form_06(self):
        self.driver.get("http://localhost/web/index.html")

        firstname_input = self.driver.find_element(By.ID, "firstname")
        lastname_input = self.driver.find_element(By.ID, "lastname")
        age_input = self.driver.find_element(By.ID, "age")
        
        firstname_input.send_keys("John")
        lastname_input.send_keys("canoncan")
        age_input.send_keys("75")

        submit_button = self.driver.find_element(By.TAG_NAME, "button")
        submit_button.click()

        result = self.driver.find_element(By.ID, "fromname").text

        print(self.driver.title)

        self.assertEqual("Customer Detail", result)
        self.driver.save_screenshot("img/test_customer_form_06.png")

    def test_customer_form_08(self):
        self.driver.get("http://localhost/web/index.html")

        firstname_input = self.driver.find_element(By.ID, "firstname")
        lastname_input = self.driver.find_element(By.ID, "lastname")
        age_input = self.driver.find_element(By.ID, "age")
        
        firstname_input.send_keys("johnjohn")
        lastname_input.send_keys("cano")
        age_input.send_keys("75")

        submit_button = self.driver.find_element(By.TAG_NAME, "button")
        submit_button.click()

        result = self.driver.find_element(By.ID, "fromname").text

        print(self.driver.title)

        self.assertEqual("Customer Detail", result)
        self.driver.save_screenshot("img/test_customer_form_08.png")
    
    def test_customer_form_010(self):
        self.driver.get("http://localhost/web/index.html")

        firstname_input = self.driver.find_element(By.ID, "firstname")
        lastname_input = self.driver.find_element(By.ID, "lastname")
        age_input = self.driver.find_element(By.ID, "age")
        
        firstname_input.send_keys("johnjohn")
        lastname_input.send_keys("cannoncancannoncanc")
        age_input.send_keys("0")

        submit_button = self.driver.find_element(By.TAG_NAME, "button")
        submit_button.click()

        result = self.driver.find_element(By.ID, "fromname").text

        print(self.driver.title)

        self.assertEqual("Customer Detail", result)
        self.driver.save_screenshot("img/test_customer_form_10.png")

    def test_customer_form_011(self):
        self.driver.get("http://localhost/web/index.html")

        firstname_input = self.driver.find_element(By.ID, "firstname")
        lastname_input = self.driver.find_element(By.ID, "lastname")
        age_input = self.driver.find_element(By.ID, "age")
        
        firstname_input.send_keys("johnjohn")
        lastname_input.send_keys("cannoncan")
        age_input.send_keys("151")

        submit_button = self.driver.find_element(By.TAG_NAME, "button")
        submit_button.click()

        result = self.driver.find_element(By.ID, "fromname").text
        print(self.driver.title)

        self.assertEqual("Customer Detail", result)
        self.driver.save_screenshot("img/test_customer_form_11.png")

if __name__ == "__main__":
    unittest.main()

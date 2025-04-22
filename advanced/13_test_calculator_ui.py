import unittest
from selenium import webdriver
from selenium.webdriver.common.by import By


#  group related test methods into test-class
class CalculatorTests(unittest.TestCase):
    
    def setUp(self):
        self.driver = webdriver.Chrome()
        self.driver.get("http://127.0.0.1:5500/web-calculator/")
        self.driver.set_window_size(1280, 800)

    def test_title(self):
        self.assertIn("Calculator", self.driver.title)

    def test_addition(self):
        driver = self.driver
        driver.find_element(By.XPATH, "//button[text()='3']").click()
        driver.find_element(By.XPATH, "//button[text()='+']").click()
        driver.find_element(By.XPATH, "//button[text()='4']").click()
        driver.find_element(By.XPATH, "//button[text()='=']").click()
        result = driver.find_element(By.ID, "display").text
        self.assertEqual(result, "7")

    @unittest.skip("Feature not ready yet")
    def test_multiplication(self):
        pass  # Placeholder for future test

    def tearDown(self):
        self.driver.quit()

if __name__ == '__main__':
    unittest.main()

import unittest
from selenium import webdriver
from selenium.webdriver.common.by import By
import time

class CalculatorTests(unittest.TestCase):

    def setUp(self):
        self.driver = webdriver.Chrome()
        self.driver.set_window_size(1280, 800)
        self.driver.get("http://127.0.0.1:5500/web-calculator/index.html")
        time.sleep(1)

    def tearDown(self):
        self.driver.quit()

    def test_addition(self):
        driver = self.driver
        driver.find_element(By.XPATH, "//button[text()='5']").click()
        driver.find_element(By.XPATH, "//button[text()='+']").click()
        driver.find_element(By.XPATH, "//button[text()='2']").click()
        driver.find_element(By.XPATH, "//button[text()='=']").click()

        time.sleep(1)
        result = driver.find_element(By.ID, "display").text.strip()
        self.assertEqual(result, "7", "Expected 5 + 2 = 7")

    def test_subtraction(self):
        driver = self.driver
        driver.find_element(By.XPATH, "//button[text()='9']").click()
        driver.find_element(By.XPATH, "//button[text()='−']").click()
        driver.find_element(By.XPATH, "//button[text()='4']").click()
        driver.find_element(By.XPATH, "//button[text()='=']").click()

        time.sleep(1)
        result = driver.find_element(By.ID, "display").text.strip()
        self.assertEqual(result, "5", "Expected 9 − 4 = 5")

if __name__ == "__main__":
    unittest.main()

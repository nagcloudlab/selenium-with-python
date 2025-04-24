

from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.keys import Keys

class BasePage:
    def __init__(self, driver):
        self.driver = driver

    def click(self, by, locator):
        WebDriverWait(self.driver, 10).until(EC.element_to_be_clickable((by, locator))).click()

    def type(self, by, locator, text):
        WebDriverWait(self.driver, 10).until(EC.presence_of_element_located((by, locator))).send_keys(text)
        WebDriverWait(self.driver, 10).until(EC.presence_of_element_located((by, locator))).send_keys(Keys.RETURN)

    def get_elements(self, by, locator):
        return self.driver.find_elements(by, locator)

    def get_texts(self, by, locator):
        return [el.text for el in self.get_elements(by, locator)]


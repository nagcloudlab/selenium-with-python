from selenium import webdriver
from selenium.webdriver.common.by import By
import time

driver = webdriver.Chrome()
driver.get("http://127.0.0.1:5500/web-calculator/index.html")

# XPath for buttons by visible text
driver.find_element(By.XPATH, "//button[text()='8']").click()
driver.find_element(By.XPATH, "//button[text()='×']").click()
driver.find_element(By.XPATH, "//button[text()='5']").click()
driver.find_element(By.XPATH, "//button[text()='=']").click()

# CSS Selector to fetch the result display
time.sleep(1)
display = driver.find_element(By.CSS_SELECTOR, "#display")
print("Displayed Result:", display.text)

# Assertion
assert display.text.strip() == "40", "❌ Incorrect result!"

driver.quit()

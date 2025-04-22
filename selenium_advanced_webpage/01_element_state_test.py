from selenium import webdriver
from selenium.webdriver.common.by import By
import time

driver = webdriver.Chrome()
driver.set_window_size(1280, 800)
driver.get("http://127.0.0.1:5500/selenium_advanced_webpage/index.html")

time.sleep(1)

# Update the ID to match actual HTML
input_field = driver.find_element(By.ID, "emailInput")
assert input_field.is_displayed(), "❌ Email input is not visible"
print("✅ Email input is visible")

submit_btn = driver.find_element(By.ID, "submitBtn")
assert submit_btn.is_enabled(), "❌ Submit button is not enabled"
print("✅ Submit button is enabled")

checkbox = driver.find_element(By.ID, "agreeTerms")
checkbox.click()
time.sleep(0.5)
assert checkbox.is_selected(), "❌ Checkbox is not selected after click"
print("✅ Checkbox selection working as expected")

driver.quit()

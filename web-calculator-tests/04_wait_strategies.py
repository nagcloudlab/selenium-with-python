from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time

# Launch driver
driver = webdriver.Chrome()

# Implicit wait applies to all find_element calls
driver.implicitly_wait(5)

# Open calculator page
driver.get("http://127.0.0.1:5500/web-calculator/index.html")

# Static wait — bad practice but easy for demo
time.sleep(1)

# Click 9 - 4 =
driver.find_element(By.XPATH, "//button[text()='9']").click()
driver.find_element(By.XPATH, "//button[text()='−']").click()
driver.find_element(By.XPATH, "//button[text()='4']").click()
driver.find_element(By.XPATH, "//button[text()='=']").click()

# Explicit wait for result to appear
wait = WebDriverWait(driver, 10)
result = wait.until(EC.text_to_be_present_in_element((By.ID, "display"), "5"))

# Read result
display = driver.find_element(By.ID, "display")
print("Displayed Result:", display.text)

# Validate
assert display.text.strip() == "5", "❌ Subtraction failed"

driver.quit()

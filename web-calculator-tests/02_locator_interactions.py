from selenium import webdriver
from selenium.webdriver.common.by import By
import time

# Setup driver
driver = webdriver.Chrome()
driver.get("http://127.0.0.1:5500/web-calculator/index.html")

# Click 7 + 3 =
driver.find_element(By.XPATH, "//button[text()='7']").click()
driver.find_element(By.XPATH, "//button[text()='+']").click()
driver.find_element(By.XPATH, "//button[text()='3']").click()
driver.find_element(By.XPATH, "//button[text()='=']").click()

# Pause to view result
time.sleep(1)

# Get the result text
display = driver.find_element(By.ID, "display")
print("Displayed Result:", display.text)

# Validate it
assert display.text.strip() == "10", "❌ Calculation failed!"

# Close browser
driver.quit()

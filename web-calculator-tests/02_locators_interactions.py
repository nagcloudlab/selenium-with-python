from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
import time


# Launch the browser
driver= webdriver.Chrome(service=Service(), options=Options())

# Navigate to the web calculator page
driver.get("http://127.0.0.1:5500/web-calculator/index.html")

# Wait for the page to load
time.sleep(2)

# click 7 + 3 =
driver.find_element(By.XPATH, "//button[text()='7']").click()
driver.find_element(By.XPATH, "//button[text()='+']").click()
driver.find_element(By.XPATH, "//button[text()='3']").click()
driver.find_element(By.XPATH, "//button[text()='=']").click()

# Pause for a moment to see the result
time.sleep(2)

# display = driver.find_element(By.XPATH, "//input[@id='display']")
display= driver.find_element(By.CSS_SELECTOR, "#display")
# Check if the result is correct
assert display.text.strip() == "10", "Result is incorrect"
# Print the result
print("Result:", display.text)
# Check if the calculator is displayed
driver.quit()
# Close the browser
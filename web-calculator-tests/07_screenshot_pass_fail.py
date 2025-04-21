from selenium import webdriver
from selenium.webdriver.common.by import By
import time

# Launch driver
driver = webdriver.Chrome()

# Open your calculator
driver.get("http://127.0.0.1:5500/web-calculator/index.html")
driver.set_window_size(1920, 1080)  # Prevents cropping in headless/full screen

# Do 3 + 2 =
driver.find_element(By.XPATH, "//button[text()='3']").click()
driver.find_element(By.XPATH, "//button[text()='+']").click()
driver.find_element(By.XPATH, "//button[text()='2']").click()
driver.find_element(By.XPATH, "//button[text()='=']").click()

# Give time for result to render
time.sleep(1)

# Capture display element safely
display = driver.find_element(By.ID, "display")

# Scroll the element into view to avoid cutoff
driver.execute_script("arguments[0].scrollIntoView(true);", display)
time.sleep(0.3)

# Read result
result = display.text.strip()

# Take screenshots based on result
try:
    assert result == "5", f"Expected 5, but got {result}"
    display.screenshot("display_pass.png")          # Element screenshot
    driver.save_screenshot("page_pass.png")         # Full page screenshot
    print("✅ Test Passed. Screenshots saved.")
except AssertionError as e:
    display.screenshot("display_fail.png")          # Element screenshot
    driver.save_screenshot("page_fail.png")         # Full page screenshot
    print("❌ Test Failed:", str(e))
    print("Screenshots saved for investigation.")

driver.quit()

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options
import time

# Set up Chrome headless
options = Options()
options.add_argument("--headless")
options.add_argument("--disable-gpu")
options.add_argument("--window-size=1920,1080")  # Important for visibility in headless

driver = webdriver.Chrome(options=options)
driver.get("http://127.0.0.1:5500/web-calculator/index.html")

# Perform: 9 - 4 =
driver.find_element(By.XPATH, "//button[text()='9']").click()
driver.find_element(By.XPATH, "//button[text()='−']").click()
driver.find_element(By.XPATH, "//button[text()='4']").click()
driver.find_element(By.XPATH, "//button[text()='=']").click()

time.sleep(1)

# Capture result
display = driver.find_element(By.ID, "display")
driver.execute_script("arguments[0].scrollIntoView(true);", display)

result = display.text.strip()
display.screenshot("headless_display.png")

if result == "5":
    print("✅ Headless Test Passed: 9 − 4 = 5")
else:
    print(f"❌ Test Failed. Got {result} instead.")

print("Screenshot saved as headless_display.png")

driver.quit()

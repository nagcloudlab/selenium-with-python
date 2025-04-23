from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import time

driver = webdriver.Chrome()
driver.set_window_size(1280, 800)
driver.get("http://127.0.0.1:5500/web-calculator/index.html")

time.sleep(1)

# ✅ Click 7 + 3
driver.find_element(By.XPATH, "//button[text()='7']").click()
driver.find_element(By.XPATH, "//button[text()='+']").click()
driver.find_element(By.XPATH, "//button[text()='3']").click()

# 🔑 Simulate pressing Enter key using send_keys on last button
equal_btn = driver.find_element(By.XPATH, "//button[text()='=']")
equal_btn.send_keys(Keys.ENTER)

# Wait for calculation to show
time.sleep(1)

# ✅ Simulate clearing using Backspace key (fake scenario — visual demo)
# In your app, the result is not typed — but let's show keyboard key anyway
display = driver.find_element(By.ID, "display")
display_text = display.text.strip()
print("Current Display:", display_text)

# Take screenshot for visual proof
display.screenshot("keyboard_result.png")

# ✅ Optional: simulate Tab key to jump focus
driver.find_element(By.ID, "themeSelector").send_keys(Keys.TAB)
print("✅ Tab key sent to theme dropdown")

driver.quit()

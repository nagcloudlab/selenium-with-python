from selenium import webdriver
from selenium.webdriver.common.by import By
import time

# Setup
driver = webdriver.Chrome()
driver.set_window_size(1280, 800)
driver.get("http://127.0.0.1:5500/web-ui/index.html")
time.sleep(1)

# 1. Trigger a JS Alert (via custom alert button)
alert_btn = driver.find_element(By.XPATH, "//button[contains(text(),'Trigger Alert')]")
alert_btn.click()
time.sleep(1)

# Switch to alert and handle
alert = driver.switch_to.alert
print("🔔 Alert Text:", alert.text)
alert.accept()
print("✅ Alert accepted.")

# 2. Toggle Disable All Buttons
disable_switch = driver.find_element(By.ID, "disableSwitch")
disable_switch.click()
time.sleep(1)

# 3. Check if buttons are disabled
buttons = driver.find_elements(By.CSS_SELECTOR, ".btn-wide:not(.btn-info)")
disabled = all(btn.get_attribute("disabled") == "true" or btn.get_attribute("disabled") == "disabled" for btn in buttons)

assert disabled, "❌ Not all calculator buttons are disabled."
print("✅ All buttons disabled as expected.")

# 4. Try interacting with input (should still work)
display = driver.find_element(By.ID, "display")
assert display.is_displayed() and display.text is not None
print("🧪 Display field is still visible and readable.")

# Optional Screenshot
driver.save_screenshot("alert_disabled_check.png")
print("📸 Screenshot saved as 'alert_disabled_check.png'")

driver.quit()

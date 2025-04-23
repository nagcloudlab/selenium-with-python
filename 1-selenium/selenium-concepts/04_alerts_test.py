from selenium import webdriver
from selenium.webdriver.common.by import By
import time

driver = webdriver.Chrome()
driver.get("http://127.0.0.1:5500/selenium-concepts/index.html")
driver.set_window_size(1280, 800)

# Scroll into view before clicking to avoid click interception
alert_btn = driver.find_element(By.XPATH, "//button[text()='Show Alert']")
driver.execute_script("arguments[0].scrollIntoView(true);", alert_btn)
time.sleep(0.5)  # slight pause for scroll animation
alert_btn.click()

# Handle JavaScript Alert
alert = driver.switch_to.alert
print("🔔 Alert Text:", alert.text)
alert.accept()
print("✅ Alert handled successfully.")

driver.quit()

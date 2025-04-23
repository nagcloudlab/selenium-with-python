from selenium import webdriver
from selenium.webdriver.common.by import By
import time

driver = webdriver.Chrome()
driver.get("http://127.0.0.1:5500/web-calculator/index.html")

# ✅ Validate Page Title
print("Page Title:", driver.title)
assert "Calculator" in driver.title, "❌ Title does not contain 'Calculator'"

# ✅ Validate Current URL
print("Current URL:", driver.current_url)
assert "127.0.0.1" in driver.current_url, "❌ Unexpected URL"

# ✅ Interact and Validate Result Text
driver.find_element(By.XPATH, "//button[text()='6']").click()
driver.find_element(By.XPATH, "//button[text()='+']").click()
driver.find_element(By.XPATH, "//button[text()='4']").click()
driver.find_element(By.XPATH, "//button[text()='=']").click()

time.sleep(1)
display = driver.find_element(By.ID, "display")
print("Displayed Text:", display.text)
assert display.text.strip() == "10", "❌ Result mismatch!"

# ✅ Validate CSS Properties
color = display.value_of_css_property("color")
background = display.value_of_css_property("background-color")
print("Display Color:", color)
print("Background Color:", background)

# ✅ Navigation Controls
driver.refresh()
driver.back()     # No previous page in this context, safe fallback
driver.forward()

driver.quit()

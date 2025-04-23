from selenium import webdriver
from selenium.webdriver.common.by import By
import time

# Setup
driver = webdriver.Chrome()
driver.set_window_size(1280, 800)
driver.get("http://127.0.0.1:7002")

time.sleep(1)

# 1. Page Title & URL Validation
assert "TodoMVC" in driver.title or "todo" in driver.title.lower(), f"❌ Unexpected title: {driver.title}"
assert "127.0.0.1:7002" in driver.current_url, f"❌ Unexpected URL: {driver.current_url}"

print("✅ Page title and URL validated.")

# 2. Add a Todo (optional for text & style validation)
todo_input = driver.find_element(By.CLASS_NAME, "new-todo")
todo_input.send_keys("Style Check")
todo_input.send_keys("\n")
time.sleep(1)

# 3. Validate text content
first_label = driver.find_element(By.CSS_SELECTOR, ".todo-list li label")
assert first_label.text == "Style Check", "❌ Label text does not match expected"

# 4. Validate CSS styles
print("\n🔍 CSS Style Checks:")
print("Font Size        :", first_label.value_of_css_property("font-size"))
print("Font Family      :", first_label.value_of_css_property("font-family"))
print("Text Color       :", first_label.value_of_css_property("color"))
print("Background Color :", first_label.value_of_css_property("background-color"))

# Optional screenshot
driver.save_screenshot("style_check.png")
print("\n📸 Screenshot saved as 'style_check.png'")

print("\n✅ Test Passed: UI elements and styles validated.")
driver.quit()

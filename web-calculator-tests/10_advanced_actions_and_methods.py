from selenium import webdriver
from selenium.webdriver.common.by import By
import time

driver = webdriver.Chrome()
driver.set_window_size(1280, 800) # Set window size
driver.get("http://127.0.0.1:5500/web-calculator/index.html")

# Let the page load
time.sleep(1)

# ✅ 1. is_displayed() and is_enabled()
display = driver.find_element(By.ID, "display")
print("Is display visible?", display.is_displayed())
print("Is display enabled?", display.is_enabled())

# ✅ 2. get_attribute()
print("Display tag name:", display.tag_name)
readonly_status = display.get_attribute("readonly")
print("Is display readonly?", readonly_status)  # Will print None if not set

# ✅ 3. value_of_css_property()
text_color = display.value_of_css_property("color")
bg_color = display.value_of_css_property("background-color")
print("Text color:", text_color)
print("Background color:", bg_color)

# ✅ 4. Click a few buttons
driver.find_element(By.XPATH, "//button[text()='7']").click()
driver.find_element(By.XPATH, "//button[text()='×']").click()
driver.find_element(By.XPATH, "//button[text()='8']").click()
driver.find_element(By.XPATH, "//button[text()='=']").click()

time.sleep(1)

# ✅ 5. Read and assert value
result = display.text.strip()
print("Calculation result:", result)
assert result == "56", "Expected 7 × 8 = 56"

# ✅ 6. Screenshot element for reference
display.screenshot("display_css_validation.png")

driver.quit()

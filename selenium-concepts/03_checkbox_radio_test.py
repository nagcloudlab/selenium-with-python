from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

driver = webdriver.Chrome()
driver.get("http://127.0.0.1:5500/selenium-concepts/index.html")
driver.set_window_size(1280, 800)

wait = WebDriverWait(driver, 5)

# ✅ Click the checkbox
checkbox = driver.find_element(By.ID, "subscribe")
checkbox.click()

# ✅ Wait until the label is updated to show subscription status
message = wait.until(
    EC.text_to_be_present_in_element((By.ID, "optionResult"), "Subscribed")
)
assert message
print("✅ Checkbox test passed.")

# ✅ Click Male radio button
male_radio = driver.find_element(By.XPATH, "//input[@name='gender' and @value='Male']")
male_radio.click()

# ✅ Wait for text update
message2 = wait.until(
    EC.text_to_be_present_in_element((By.ID, "optionResult"), "Selected: Male")
)
assert message2
print("✅ Radio button test passed.")

driver.quit()

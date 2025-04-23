from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

driver = webdriver.Chrome()
driver.get("http://127.0.0.1:5500/selenium-concepts/index.html")
driver.set_window_size(1280, 900)

wait = WebDriverWait(driver, 10)

# Locate the button
load_btn = driver.find_element(By.XPATH, "//button[text()='Load Message']")
# load_btn.click()
# Scroll and click using JavaScript (ignores overlays, reliable!)
driver.execute_script("arguments[0].scrollIntoView(true);", load_btn)
driver.execute_script("arguments[0].click();", load_btn)

# Wait for message to appear
msg = wait.until(EC.visibility_of_element_located((By.ID, "delayedMsg")))
assert "Successfully Loaded" in msg.text

print("✅ Test Passed: Dynamic message appeared.")

driver.quit()

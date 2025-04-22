from selenium import webdriver
from selenium.webdriver.common.by import By

driver = webdriver.Chrome()
driver.get("http://127.0.0.1:5500/selenium-concepts/index.html")

disabled_btn = driver.find_element(By.ID, "disabledBtn")
readonly_input = driver.find_element(By.CSS_SELECTOR, "input[readonly]")

assert not disabled_btn.is_enabled()
assert readonly_input.get_attribute("readonly") is not None
print("✅ Disabled and readonly test passed.")

driver.quit()
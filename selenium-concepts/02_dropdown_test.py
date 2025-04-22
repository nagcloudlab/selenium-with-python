from selenium import webdriver
from selenium.webdriver.common.by import By
import time

driver = webdriver.Chrome()
driver.get("http://127.0.0.1:5500/selenium-concepts/index.html")

dropdown = driver.find_element(By.ID, "language")
dropdown.click()
dropdown.find_element(By.XPATH, "//option[text()='Python']").click()

time.sleep(1)
msg = driver.find_element(By.ID, "languageResult").text
assert "Python" in msg
print("✅ Dropdown test passed.")

driver.quit()
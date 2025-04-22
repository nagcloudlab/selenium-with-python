from selenium import webdriver
from selenium.webdriver.common.by import By
import time

driver = webdriver.Chrome()
driver.get("http://127.0.0.1:5500/selenium-concepts/index.html")

input_box = driver.find_element(By.ID, "username")
input_box.send_keys("Nag")

submit_button = driver.find_element(By.XPATH, "//button[text()='Submit']")
submit_button.click()

time.sleep(1)
message = driver.find_element(By.ID, "usernameResult").text
assert "Nag" in message
print("✅ Text input test passed.")

driver.quit()
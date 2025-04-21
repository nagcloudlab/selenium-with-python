from selenium import webdriver
from selenium.webdriver.common.by import By
import time

driver = webdriver.Chrome()
driver.get("http://127.0.0.1:5500/web-calculator/index.html")

# 👉 Click 2 + 2 =
driver.find_element(By.XPATH, "//button[text()='2']").click()
driver.find_element(By.XPATH, "//button[text()='+']").click()
driver.find_element(By.XPATH, "//button[text()='2']").click()
driver.find_element(By.XPATH, "//button[text()='=']").click()

time.sleep(1)

# ✅ Toggle disable switch (simulate checking is_enabled)
disable_toggle = driver.find_element(By.ID, "disableSwitch")
disable_toggle.click()
time.sleep(1)

button = driver.find_element(By.XPATH, "//button[text()='7']")
print("Is '7' button enabled?", button.is_enabled())  # should print False

# ✅ Interact with dropdown and trigger alert
dropdown = driver.find_element(By.ID, "themeSelector")
dropdown.click()
dropdown.find_element(By.XPATH, "//option[@value='dark']").click()

# ✅ Handle the alert that appears
alert = driver.switch_to.alert
print("Dropdown alert says:", alert.text)
alert.accept()

# ✅ Trigger custom alert
driver.find_element(By.XPATH, "//button[text()='Trigger Alert']").click()
alert = driver.switch_to.alert
print("Custom Alert says:", alert.text)
alert.accept()

# Done
driver.quit()

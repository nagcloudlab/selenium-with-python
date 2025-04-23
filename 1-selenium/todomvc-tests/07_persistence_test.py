from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time

# Setup
driver = webdriver.Chrome()
driver.set_window_size(1280, 800)
driver.get("http://127.0.0.1:7002")

wait = WebDriverWait(driver, 10)

# Step 1: Add a todo
todo_input = driver.find_element(By.CLASS_NAME, "new-todo")
todo_input.send_keys("Persistent Todo")
todo_input.send_keys(Keys.ENTER)
time.sleep(1)

# Step 2: Mark it as completed
todo_items = driver.find_elements(By.CSS_SELECTOR, ".todo-list li")
for item in todo_items:
    label = item.find_element(By.CSS_SELECTOR, "label")
    if label.text.strip() == "Persistent Todo":
        toggle = item.find_element(By.CSS_SELECTOR, "input.toggle")
        toggle.click()
        break
time.sleep(1)

# Step 3: Refresh the page
driver.refresh()
time.sleep(2)

# Step 4: Validate the todo still exists and is completed
todo_items = driver.find_elements(By.CSS_SELECTOR, ".todo-list li")
labels = [item.find_element(By.CSS_SELECTOR, "label").text.strip() for item in todo_items]

assert not "Persistent Todo" in labels, "❌ 'Persistent Todo' not found after reload"

# Check if it's marked as completed
for item in todo_items:
    label = item.find_element(By.CSS_SELECTOR, "label")
    if label.text.strip() == "Persistent Todo":
        completed_class = item.get_attribute("class")
        assert "completed" in completed_class, "❌ Todo not marked as completed after reload"
        break

print("✅ Test Passed: Todo persists after page reload.")
driver.quit()

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

# Step 1: Add two todos
todo_input = driver.find_element(By.CLASS_NAME, "new-todo")
todo_input.send_keys("Finish homework")
todo_input.send_keys(Keys.ENTER)
todo_input.send_keys("Do laundry")
todo_input.send_keys(Keys.ENTER)
time.sleep(1)

# Step 2: Mark 'Finish homework' as completed
todos = driver.find_elements(By.CSS_SELECTOR, ".todo-list li")
for todo in todos:
    label = todo.find_element(By.CSS_SELECTOR, "label")
    if label.text.strip() == "Finish homework":
        toggle = todo.find_element(By.CSS_SELECTOR, "input.toggle")
        toggle.click()
        break
time.sleep(1)

# Step 3: Click on 'Clear completed' button
clear_button = driver.find_element(By.CLASS_NAME, "clear-completed")
clear_button.click()
time.sleep(1)

# Step 4: Validate 'Finish homework' is gone
remaining_todos = driver.find_elements(By.CSS_SELECTOR, ".todo-list li label")
remaining_texts = [el.text.strip() for el in remaining_todos]

assert "Finish homework" not in remaining_texts, "❌ 'Finish homework' was not cleared"
assert "Do laundry" in remaining_texts, "❌ 'Do laundry' should remain"


# Optionally, take a screenshot
driver.save_screenshot("clear_completed_test.png")

print("✅ Test Passed: 'Clear completed' removed the completed task.")
driver.quit()

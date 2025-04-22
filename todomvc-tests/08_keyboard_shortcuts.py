from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import time

# Setup
driver = webdriver.Chrome()
driver.set_window_size(1280, 800)
driver.get("http://127.0.0.1:7002")

time.sleep(1)

# Step 1: Focus the input field and type using keyboard
todo_input = driver.find_element(By.CLASS_NAME, "new-todo")
todo_input.click()  # Focus
todo_input.send_keys("Keyboard shortcut test")
todo_input.send_keys(Keys.ENTER)
time.sleep(1)

# Step 2: Validate the todo is added
todos = driver.find_elements(By.CSS_SELECTOR, ".todo-list li label")
labels = [el.text.strip() for el in todos]

assert "Keyboard shortcut test" in labels, "❌ Todo not added via keyboard"

print("✅ Test Passed: Todo added using keyboard shortcuts.")
driver.quit()

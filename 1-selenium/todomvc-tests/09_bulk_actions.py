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

# Step 1: Add multiple todos
todo_input = driver.find_element(By.CLASS_NAME, "new-todo")
tasks = ["Clean room", "Buy groceries", "Write tests"]
for task in tasks:
    todo_input.send_keys(task)
    todo_input.send_keys(Keys.ENTER)
    time.sleep(0.5)

# Step 2: Mark each todo as completed manually
todos = driver.find_elements(By.CSS_SELECTOR, ".todo-list li")
for todo in todos:
    toggle = todo.find_element(By.CSS_SELECTOR, "input.toggle")
    toggle.click()
    time.sleep(0.3)
    assert "completed" in todo.get_attribute("class"), "❌ Todo not marked as completed"

# Step 3: Click 'Clear completed'
try:
    clear_button = wait.until(EC.element_to_be_clickable((By.CLASS_NAME, "clear-completed")))
    clear_button.click()
    print("✅ Clicked 'Clear completed' button.")
except:
    print("❌ 'Clear completed' button not found or clickable.")
    driver.quit()
    exit(1)

# Step 4: Verify all todos are cleared
time.sleep(1)
remaining = driver.find_elements(By.CSS_SELECTOR, ".todo-list li")
assert len(remaining) == 0, f"❌ Expected 0 todos, but found {len(remaining)}"

print("✅ Test Passed: All todos completed and cleared.")
driver.quit()

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
todo_input.send_keys("First Task")
todo_input.send_keys(Keys.ENTER)
todo_input.send_keys("Second Task")
todo_input.send_keys(Keys.ENTER)
time.sleep(1)

# Step 2: Mark 'First Task' as completed
todos = driver.find_elements(By.CSS_SELECTOR, ".todo-list li")
for todo in todos:
    label = todo.find_element(By.CSS_SELECTOR, "label")
    if label.text.strip() == "First Task":
        toggle = todo.find_element(By.CSS_SELECTOR, "input.toggle")
        toggle.click()
        break
time.sleep(1)

# Step 3: Click on 'Completed' tab
driver.find_element(By.LINK_TEXT, "Completed").click()
time.sleep(1)

# Step 4: Validate only 'First Task' is shown
completed_items = driver.find_elements(By.CSS_SELECTOR, ".todo-list li")
assert len(completed_items) == 1, f"❌ Expected 1 completed item, got {len(completed_items)}"
completed_label = completed_items[0].find_element(By.CSS_SELECTOR, "label").text.strip()
assert completed_label == "First Task", f"❌ Expected 'First Task', got '{completed_label}'"

# Step 5: Click on 'Active' tab
driver.find_element(By.LINK_TEXT, "Active").click()
time.sleep(1)

# Step 6: Validate only 'Second Task' is shown
active_items = driver.find_elements(By.CSS_SELECTOR, ".todo-list li")
assert len(active_items) == 1, f"❌ Expected 1 active item, got {len(active_items)}"
active_label = active_items[0].find_element(By.CSS_SELECTOR, "label").text.strip()
assert active_label == "Second Task", f"❌ Expected 'Second Task', got '{active_label}'"

# Step 7: Click on 'All' tab
driver.find_element(By.LINK_TEXT, "All").click()
time.sleep(1)

# Step 8: Validate both todos are visible again
all_items = driver.find_elements(By.CSS_SELECTOR, ".todo-list li")
assert len(all_items) == 2, f"❌ Expected 2 items on All tab, got {len(all_items)}"

# screen capture the result
driver.save_screenshot("filter_tabs_test.png")

print("✅ Test Passed: Filter tabs working as expected.")
driver.quit()
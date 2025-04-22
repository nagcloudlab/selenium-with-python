from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import time

driver = webdriver.Chrome()
driver.get("http://127.0.0.1:7002")  # Adjust the URL if necessary

time.sleep(2)  # Wait for the page to load


#Locate the input field for adding a new todo item
input_field = driver.find_element(By.CSS_SELECTOR, "input.new-todo")
# Add a new todo item
input_field.send_keys("Buy groceries")
input_field.send_keys(Keys.RETURN)  # Press Enter to add the todo item
# Wait for a moment to ensure the item is added
time.sleep(2)

checkbox = driver.find_element(By.CSS_SELECTOR, "ul.todo-list li input.toggle")
# Check the checkbox to mark the todo item as completed
checkbox.click()
# Wait for a moment to ensure the item is marked as completed
time.sleep(2)

# Verify that the new todo item is marked as completed
completed_todo_item = driver.find_element(By.CSS_SELECTOR, "ul.todo-list li")
classes=completed_todo_item.get_attribute("class")
assert "completed" in classes, "Todo item not marked as completed"


# Optionally, screen capture the result
driver.save_screenshot("complete_todo_test.png")
print("Todo item added successfully and screenshot saved.")
# Close the browser
driver.quit()
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.action_chains import ActionChains
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

# Verify that the new todo item is marked as completed
todo_item = driver.find_element(By.CSS_SELECTOR, "ul.todo-list li")
delete_button=todo_item.find_element(By.CSS_SELECTOR, ".destroy")


actions = ActionChains(driver)
# Move the mouse to the delete button
actions.move_to_element(todo_item).perform()
# Wait for the delete button to be visible
time.sleep(1)   

# Click the delete button to remove the todo item
delete_button.click()
# Wait for a moment to ensure the item is deleted
time.sleep(2)

# Verify that the todo item is no longer present in the list
todo_items = driver.find_elements(By.CSS_SELECTOR, "ul.todo-list li")
assert not any("Buy groceries" in item.text for item in todo_items), "Todo item was not deleted successfully"


# Optionally, screen capture the result
driver.save_screenshot("delete_todo_test.png")
print("Todo item added successfully and screenshot saved.")
# Close the browser
driver.quit()
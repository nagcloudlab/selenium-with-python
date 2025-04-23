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


# Locate the newly added todo item
todo_item = driver.find_element(By.CSS_SELECTOR, "ul.todo-list li")
label = todo_item.find_element(By.CSS_SELECTOR, "label")
# Double-click the label to edit the todo item
actions = ActionChains(driver)
actions.double_click(label).perform()
# Wait for the edit input to appear
time.sleep(1)
# Locate the edit input field
edit_input = driver.find_element(By.CSS_SELECTOR, "input.edit")
# Clear the existing text and enter new text
edit_input.clear()
edit_input.send_keys("Buy groceries and cook dinner")
edit_input.send_keys(Keys.RETURN)  # Press Enter to save the changes
# Wait for a moment to ensure the item is updated
time.sleep(2)
# Verify that the todo item has been updated
updated_todo_item = driver.find_element(By.CSS_SELECTOR, "ul.todo-list li label")
assert updated_todo_item.text == "Buy groceries and cook dinner", "Todo item not updated correctly"
# Optionally, you can also check if the edit input is no longer visible
edit_input = driver.find_elements(By.CSS_SELECTOR, "input.edit")
assert len(edit_input) == 0, "Edit input is still visible after saving changes"

# Optionally, screen capture the result
driver.save_screenshot("edit_todo_test.png")
print("Todo item added successfully and screenshot saved.")
# Close the browser
driver.quit()



# Flow

# step 1: -> Locate Label "Buy groceries"
# step 2: -> Double click on the label
# Stale Risk -> Don't use old <li> element or the label element
# step 3: -> Wait for 'li.editing' to appear
# step 4: -> Use JS to safely update 'edit' element
# step 5: -> Re-locate '.edit' freshly and  press enter
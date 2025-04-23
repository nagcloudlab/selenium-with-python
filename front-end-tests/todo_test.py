from selenium.webdriver.common.by import By
import time

def test_be_true():
    assert True

def test_add_todo(browser):
    # Open the application
    browser.get("http://127.0.0.1:8080/")
    time.sleep(2)  # Wait for the page to load
    # Find the input field and add a new todo
    input_field = browser.find_element(By.CSS_SELECTOR, "input")
    input_field.send_keys("Buy groceries")
    input_field.send_keys("\n")  # Simulate pressing Enter key
    
    # Verify the new todo is added
    todo_list = browser.find_element(By.CSS_SELECTOR, "ul li")
    assert "Buy groceries" in todo_list.text
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import *
import time

driver = webdriver.Chrome()
driver.set_window_size(1280, 800)
driver.get("http://127.0.0.1:7002")

wait = WebDriverWait(driver, 10)
actions = ActionChains(driver)

try:
    # Step 1: Add new todo
    todo_input = wait.until(EC.presence_of_element_located((By.CLASS_NAME, "new-todo")))
    todo_input.send_keys("Fix this flaky test")
    todo_input.send_keys(Keys.ENTER)
    time.sleep(1)

    # Step 2: Locate label and double-click it
    label_xpath = "//label[normalize-space()='Fix this flaky test']"
    label = wait.until(EC.element_to_be_clickable((By.XPATH, label_xpath)))
    actions.double_click(label).perform()

    # Step 3: Use JS to safely enter new text in edit field
    time.sleep(0.5)
    driver.execute_script("""
        const input = document.querySelector('li.editing .edit');
        input.value = 'Fixed using JS patch';
    """)

    # Step 4: Re-grab input and press ENTER
    edit_input = wait.until(EC.element_to_be_clickable((By.CSS_SELECTOR, "li.editing .edit")))
    edit_input.send_keys(Keys.ENTER)

    # Step 5: Verify
    updated = wait.until(EC.presence_of_element_located(
        (By.XPATH, "//label[normalize-space()='Fixed using JS patch']")))
    assert updated.is_displayed()

    print("✅ Test Passed: Edited successfully with JS assist.")

except Exception as e:
    print("❌ Test Failed:", e)
    driver.save_screenshot("edit_exception_fixed.png")
    print("📸 Screenshot saved as edit_exception_fixed.png")

finally:
    driver.quit()
    print("🧹 Driver closed.")

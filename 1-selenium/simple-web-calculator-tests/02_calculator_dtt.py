from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
import time
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import csv

# service = Service(executable_path='/home/nag/drivers/chromedriver-linux64/chromedriver')

# launch the browser
driver = webdriver.Chrome()

# Navigate to the web calculator application
# Note: Make sure the web server is running and accessible at this URL
driver.get("http://127.0.0.1:5500/simple-web-calculator/index.html")

# Find the elements for the first number element
first_number_input = driver.find_element(By.ID, "input1")
# Find the elements for the second number element
second_number_input = driver.find_element(By.ID, "input2")
# Find the calculate button
calculate_button = driver.find_element(By.ID, "calculate")
# Find the operation selector
operation_selector = driver.find_element(By.ID, "operation")

with open("arith-test-data.csv", "r") as file:
    reader=csv.DictReader(file)
    for row in reader:
        # Enter the first number
        first_number_input.clear()
        first_number_input.send_keys(row["input1"])
        time.sleep(2)
        # Select the operation
        operation_selector.click()
        operation_selector.find_element(By.XPATH, f"//option[text()='{row['operation']}']").click()
        time.sleep(2)
        # Enter the second number
        second_number_input.clear()
        second_number_input.send_keys(row["input2"])
        time.sleep(2)
        # Click the calculate button
        calculate_button.click()
        time.sleep(2)
        # Get the result
        wait= WebDriverWait(driver, 1)
        result = wait.until(EC.presence_of_element_located((By.ID, "result")))
        result_value = result.text
        # Print the result
        print(f"Result of addition: {result_value}")

        # assert the result
        assert result_value == row["result"], f"Expected {row['result']} but got {result_value}"
    

# Close the browser
driver.quit()

from selenium import webdriver
from selenium.webdriver.common.by import By
import time
import openpyxl

# Load test data from Excel
workbook = openpyxl.load_workbook("calc_test_cases.xlsx")
sheet = workbook.active

# Start browser
driver = webdriver.Chrome()
driver.set_window_size(1200, 800)
driver.get("http://127.0.0.1:5500/web-calculator/index.html")

time.sleep(1)

# Map logical operator to actual button symbols on UI
operator_map = {
    '+': '+',
    '-': '−',  # Unicode minus (not regular hyphen)
    '*': '×',
    '/': '÷'
}

# Loop through Excel rows (skip header)
for row in sheet.iter_rows(min_row=2, values_only=True):
    a, op, b, expected = row

    # Clear calculator display
    driver.find_element(By.XPATH, "//button[text()='C']").click()

    # Perform operation
    try:
        driver.find_element(By.XPATH, f"//button[text()='{a}']").click()
        driver.find_element(By.XPATH, f"//button[text()='{operator_map[op]}']").click()
        driver.find_element(By.XPATH, f"//button[text()='{b}']").click()
        driver.find_element(By.XPATH, "//button[text()='=']").click()

        time.sleep(1)

        # Capture result
        result = driver.find_element(By.ID, "display").text.strip()

        if str(result) == str(expected):
            print(f"✅ {a} {op} {b} = {result} [PASS]")
        else:
            print(f"❌ {a} {op} {b} = {result} [FAIL, expected {expected}]")

    except Exception as e:
        print(f"⚠️ Error in test case {a} {op} {b}: {e}")

driver.quit()

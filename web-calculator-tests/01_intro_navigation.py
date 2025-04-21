from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
import time



# Launch the browser
driver= webdriver.Chrome(service=Service(), options=Options())

# Navigate to the web calculator page
driver.get("http://127.0.0.1:5500/web-calculator/index.html")

# Wait for the page to load
time.sleep(2)

# Print the page title
print(driver.title)

# Check if the title is correct
assert "Web Calculator" in driver.title, "Title does not match"

# Check if the calculator is displayed
driver.quit()
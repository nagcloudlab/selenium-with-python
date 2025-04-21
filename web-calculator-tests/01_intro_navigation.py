# Introduction to Automation & Selenium
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
import time

# Optional: Headless mode
# options = Options()
# options.add_argument("--headless")

# Use this if ChromeDriver is not in PATH
# service = Service("/path/to/chromedriver")

# Launch browser
driver = webdriver.Chrome()  # or webdriver.Chrome(service=service, options=options)

# Navigate to your local calculator page
driver.get("http://127.0.0.1:5500/web-calculator/index.html")

# Print the title
print("Page Title:", driver.title)

# Wait for 2 seconds
time.sleep(2)

# Close the browser
driver.quit()

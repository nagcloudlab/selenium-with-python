from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains
import time

driver = webdriver.Chrome()
driver.get("http://127.0.0.1:5500/web-calculator/index.html")
driver.set_window_size(1280, 800)
actions = ActionChains(driver)

# Wait for page to render
time.sleep(1)

# ✅ Mouse hover over a button (simulate tooltips/menus)
hover_button = driver.find_element(By.XPATH, "//button[text()='=']")
actions.move_to_element(hover_button).perform()
print("✅ Hovered over '=' button")

# ✅ Double-click a number (not required in your app, but shown for demo)
number_btn = driver.find_element(By.XPATH, "//button[text()='1']")
actions.double_click(number_btn).perform()
print("✅ Double-clicked on '1'")

# ✅ Right-click a button (context click)
plus_btn = driver.find_element(By.XPATH, "//button[text()='+']")
actions.context_click(plus_btn).perform()
print("✅ Right-clicked on '+' button")

# ✅ Click-and-hold on Clear button
clear_btn = driver.find_element(By.XPATH, "//button[text()='C']")
actions.click_and_hold(clear_btn).pause(1).release().perform()
print("✅ Click-and-hold on 'C' (then release)")

# ✅ Screenshot for demo
driver.save_screenshot("advanced_actions.png")
print("📸 Screenshot saved as advanced_actions.png")

driver.quit()

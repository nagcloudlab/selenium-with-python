

import pytest
from selenium import webdriver
from selenium.webdriver.chrome.options import Options

# @pytest.fixture
# def browser():
#     options = Options()
#     options.add_argument("--headless")  # comment out to see the browser
#     driver = webdriver.Chrome(options=options)
#     driver.implicitly_wait(5)
#     driver.maximize_window()
#     yield driver
#     driver.quit()



import pytest
from selenium import webdriver
from selenium.webdriver.chrome.options import Options as ChromeOptions
from selenium.webdriver.firefox.options import Options as FirefoxOptions


@pytest.fixture(params=["chrome","firefox"])
def browser(request):
    if request.param == "chrome":
        options = ChromeOptions()
        options.add_argument("--headless")
        driver = webdriver.Chrome(options=options)

    elif request.param == "firefox":
        options = FirefoxOptions()
        options.add_argument("--headless")
        service = webdriver.firefox.service.Service(executable_path="/home/nag/Downloads/geckodriver-v0.36.0-linux64/geckodriver")
        driver = webdriver.Firefox(options=options, service=service)
    else:
        raise ValueError(f"Unsupported browser: {request.param}")

    driver.maximize_window()
    yield driver
    driver.quit()





@pytest.hookimpl(tryfirst=True, hookwrapper=True)
def pytest_runtest_makereport(item, call):
    # Execute all other hooks to obtain the report object
    outcome = yield
    report = outcome.get_result()

    # Only take screenshot on failures
    if report.when == "call" and report.failed:
        browser = item.funcargs.get("browser")
        if browser:
            screenshot_name = f"screenshots/{item.name}.png"
            browser.save_screenshot(screenshot_name)
            print(f"\n💥 Screenshot saved to: {screenshot_name}")



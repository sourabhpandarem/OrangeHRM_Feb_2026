import pytest
import pytest
import driver
from driver import driver
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager


def pytest_addoption(parser):
    parser.addoption("--browser")


@pytest.fixture(scope="class")
def driver_setup(request):
    browser = request.config.getoption("--browser")
    if browser == "chrome":
        print("Launching Chrome Browser")
        from selenium import webdriver
        chrome_options = webdriver.ChromeOptions()

        chrome_options.add_experimental_option("prefs", {
            "credentials_enable_service": False,

            "profile.password_manager_enabled": False,
            "profile.password_manager_leak_detection": False

        }
                                               )
        driver = webdriver.Chrome(options=chrome_options)


    elif browser == "firefox":
        print("Launching Firefox Browser")
        from selenium import webdriver
        driver = webdriver.Firefox()
    elif browser == "edge":
        print("Launching Edge Browser")
        from selenium import webdriver
        driver = webdriver.Edge()
    elif browser == "headless":
        print("Launching Headless Browser")
        from selenium import webdriver
        from selenium.webdriver.chrome.options import Options
        chrome_options = Options()
        chrome_options.add_argument("--headless")
        driver = webdriver.Chrome(options=chrome_options)
    else:
        print("Invalid Browser")
        driver = None
    driver.maximize_window()
    request.cls.driver = driver
    yield driver
    driver.quit()










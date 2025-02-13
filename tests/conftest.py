import pytest
from selenium import webdriver


@pytest.fixture(params=['Firefox'], scope="class")
def fixture_setup(request):
    """Return driver browser"""
    driver = None
    if request.param == "Chrome":
        chrome_options = webdriver.ChromeOptions()
        chrome_options.add_argument("--start-maximized")
        # chrome_options.add_argument("--headless")
        driver = webdriver.Chrome(options=chrome_options)
    elif request.param == "Firefox":
        firefox_options = webdriver.FirefoxOptions()
        # firefox_options.add_argument("--headless")
        driver = webdriver.Firefox(options=firefox_options)
        driver.maximize_window()
    yield driver
    driver.quit()

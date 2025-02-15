import os
import pytest
from selenium import webdriver


@pytest.fixture(params=['Chrome'], scope='class')
def fixture_setup(request):
    """Создание драйвера браузера"""
    driver = None
    if request.param == 'Chrome':
        chrome_options = webdriver.ChromeOptions()

        download_dir = os.path.join(os.getcwd(), 'tests')
        prefs = {
            "download.default_directory": download_dir,  # Папка для загрузки
            "download.prompt_for_download": False,  # Не запрашивать подтверждение
            "download.directory_upgrade": True,  # Обновить директорию
            "safebrowsing.enabled": True  # Включить безопасный просмотр
        }
        chrome_options.add_experimental_option("prefs", prefs)

        chrome_options.add_argument('--start-maximized')
        chrome_options.add_argument('--headless')
        driver = webdriver.Chrome(options=chrome_options)
    elif request.param == 'Firefox':
        firefox_options = webdriver.FirefoxOptions()
        # firefox_options.add_argument('--headless')
        driver = webdriver.Firefox(options=firefox_options)
        driver.maximize_window()
    yield driver
    driver.quit()

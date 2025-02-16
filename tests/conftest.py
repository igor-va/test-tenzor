import os
import pytest
from selenium import webdriver


@pytest.fixture(params=['Chrome', 'Firefox'], scope='class')
def fixture_setup(request):
    """Создание драйвера браузера"""

    driver = None
    download_dir = os.path.join(os.getcwd(), 'tests')

    # Настройка драйвера 'Chrome'
    if request.param == 'Chrome':
        chrome_options = webdriver.ChromeOptions()
        prefs = {
            "download.default_directory": download_dir,  # Папка для загрузки
            "download.prompt_for_download": False,  # Не запрашивать подтверждение
            "download.directory_upgrade": True,  # Обновить директорию
            "safebrowsing.enabled": True  # Включить безопасный просмотр
        }
        chrome_options.add_experimental_option('prefs', prefs)
        chrome_options.add_argument('--start-maximized')
        chrome_options.add_argument('--headless')
        driver = webdriver.Chrome(options=chrome_options)

    # Настройка драйвера 'Firefox'
    elif request.param == 'Firefox':
        firefox_options = webdriver.FirefoxOptions()
        firefox_options.set_preference("browser.download.folderList", 2)  # '2' означает пользовательская папка
        firefox_options.set_preference("browser.download.dir", download_dir)  # Папка для загрузки
        firefox_options.set_preference("browser.helperApps.neverAsk.saveToDisk",
                                       "application/octet-stream,application/x-msdownload")  # MIME-тип '.exe' файлов
        firefox_options.add_argument('--headless')
        driver = webdriver.Firefox(options=firefox_options)
        driver.maximize_window()

    # Возвращение драйвера
    yield driver

    # Закрытие браузера
    driver.quit()

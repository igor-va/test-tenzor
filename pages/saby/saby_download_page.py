import os
import time

from ..base_page import BasePage
from locators.saby.saby_download_locators import SabyDownloadLocators


class SabyDownloadPage(BasePage):
    """Класс для хранений действий на сайте 'Saby' страницы 'Скачать"""

    def __init__(self, driver):
        super().__init__(driver)

    def click_item_plugin_web_installer(self) -> None:
        """Скачивание плагина 'Веб-установщик'"""

        current_dir = os.path.join(os.getcwd(), 'tests')

        # Удаление всех ранее загруженных файлов .exe
        for filename in os.listdir(current_dir):
            if filename.endswith('.exe'):
                file_path = os.path.join(current_dir, filename)
                try:
                    os.remove(file_path)  # Удаление файла
                except Exception as e:
                    print(f"Не удалось удалить файл {file_path}: {e}")

        BasePage.action_click(self, element=SabyDownloadLocators.loc_plugin_web_installer)

        # Ожидание загрузки файла
        def wait_for_downloads(work_dir):
            while True:
                if any([filename.endswith('.exe') for filename in os.listdir(work_dir)]):
                    break
                time.sleep(0.5)

        wait_for_downloads(current_dir)

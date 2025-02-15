from ..base_page import BasePage
from locators.saby.saby_download_locators import SabyDownloadLocators
from utilities.file_handling_utility import *


class SabyDownloadPage(BasePage):
    """Класс для хранений действий на сайте 'Saby' страницы 'Скачать"""

    def __init__(self, driver):
        super().__init__(driver)

    def click_item_plugin_web_installer(self) -> None:
        """Скачивание плагина 'Веб-установщик'"""
        current_dir = os.path.join(os.getcwd(), 'tests')
        delete_previously_uploaded_files(current_dir)  # Удаление всех ранее загруженных файлов '.exe'
        BasePage.action_click(self, element=SabyDownloadLocators.loc_plugin_web_installer)
        wait_for_download_file(current_dir)  # Ожидание загрузки файла

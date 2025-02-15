from ..base_page import BasePage
from locators.saby.saby_download_locators import SabyDownloadLocators
from utilities.file_handling_utility import *
from info.plugins import Plugins


class SabyDownloadPage(BasePage):
    """Класс для хранений действий на сайте 'Saby' страницы 'Скачать"""

    def __init__(self, driver):
        super().__init__(driver)
        self.current_dir = os.path.join(os.getcwd(), 'tests')

    def click_item_plugin_web_installer(self) -> None:
        """Скачивание плагина 'Веб-установщик'"""
        delete_previously_uploaded_files(self.current_dir)  # Удаление всех ранее загруженных файлов '.exe'
        BasePage.action_click(self, element=SabyDownloadLocators.loc_plugin_web_installer)
        wait_for_download_file(self.current_dir)  # Ожидание загрузки файла

    def verify_file_exist(self) -> bool:
        """Проверка существования скачанного файла"""
        file_status = file_exists(self.current_dir, Plugins.web_installer_name)
        if file_status:
            return True
        else:
            return False

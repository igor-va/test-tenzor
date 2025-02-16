import pytest
import allure

from pages.saby.saby_home_page import SabyHomePage
from pages.saby.saby_download_page import SabyDownloadPage
from configurations.test_data import *


@allure.feature("Тестовое задание")
@pytest.mark.ui
class TestClass:
    """Тестовый класс"""

    @allure.title("Третий сценарий")
    @allure.description("Третий сценарий тестового задания")
    @pytest.mark.tc3
    def test_three(self, fixture_setup) -> None:
        """Третий сценарий тестового задания"""

        self.driver = fixture_setup
        with allure.step(f"1. Перейти на https://sbis.ru/"):
            self.driver.get(TestDataSaby.URL_HOME)
        with allure.step(f"2. В Footer'e найти и перейти 'Скачать локальные версии'"):
            SabyHomePage(self.driver).click_item_footer_to_download_page()
        with allure.step(f"3. Скачать СБИС Плагин для windows, веб-установщик в папку с данным тестом"):
            saby_download_page = SabyDownloadPage(self.driver)
            saby_download_page.click_item_plugin_web_installer()
        with allure.step(f"4. Убедиться, что плагин скачался"):
            assert saby_download_page.verify_file_download_exist(), "Скачанный файл в каталоге не найден"
        with allure.step(f"5. Сравнить размер файла в мегабайтах, он должен совпадать с указанным на сайте"):
            assert saby_download_page.verify_file_size(), \
                f"Размер скачанного файла не совпадает с размером указанным на сайте "

import pytest
import allure
import time

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
            SabyHomePage(self.driver).click_item_footer_download_page()
        with allure.step(f"3. Скачать СБИС Плагин для windows, веб-установщик в папку с данным тестом"):
            SabyDownloadPage(self.driver).click_item_plugin_web_installer()


        # time.sleep(10)

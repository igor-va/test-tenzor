import pytest
import allure
import time

from pages.saby.saby_home_page import SabyHomePage
from pages.saby.saby_contacts_page import SabyContactsPage
from configurations.test_data import *
from info.regions import *


@allure.feature("Тестовое задание")
@pytest.mark.ui
class TestClass:
    """Тестовый класс"""

    @allure.title("Второй сценарий")
    @allure.description("Второй сценарий тестового задания")
    @pytest.mark.tc2
    def test_two(self, fixture_setup) -> None:
        """Второй сценарий тестового задания"""

        self.driver = fixture_setup
        with allure.step(f"1. Перейти на https://sbis.ru/ в раздел 'Контакты'"):
            self.driver.get(TestDataSaby.URL_HOME)
            SabyHomePage(self.driver).click_item_contacts()
        with allure.step(f"2. Проверить, что определился ваш регион (г. Санкт-Петербург) и есть список партнеров"):
            saby_contacts_page = SabyContactsPage(self.driver)
            local_region = saby_contacts_page.get_local_region()
            assert local_region == Regions.spb_region, f"Местный регион отображается некорректно"
            assert saby_contacts_page.verify_block_partners_displayed, \
                f"Блок 'Список партнеров' не найден на странице {saby_contacts_page.get_current_url()}"


        time.sleep(2)

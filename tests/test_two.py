import pytest
import allure
import time

from pages.saby.saby_home_page import SabyHomePage
from pages.saby.saby_contacts_page import SabyContactsPage
from configurations.test_data import *
from info.regions import Regions
from info.partners import Partners


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
        with (allure.step(f"2. Проверить, что определился ваш регион (г. Санкт-Петербург) и есть список партнеров")):
            saby_contacts_page = SabyContactsPage(self.driver)
            name_local_region = saby_contacts_page.get_name_local_region()
            assert name_local_region == Regions.spb_region, \
                f"Название местного региона определяется некорректно"
            name_local_partner = saby_contacts_page.get_name_local_partner()
            assert name_local_partner == Partners.spb_partner, \
                f"Блок 'Список партнеров' местного региона не найден на странице"
        with allure.step(f"3. Изменить регион на Камчатский край"):
            saby_contacts_page.change_region_to_kamchatka()

        time.sleep(2)

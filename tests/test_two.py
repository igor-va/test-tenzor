import pytest
import allure

from pages.saby.saby_home_page import SabyHomePage
from pages.saby.saby_contacts_page import SabyContactsPage
from configurations.test_data import *
from info.regions import Regions
from info.partners import Partners
from info.titles import SabyTitles


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
            SabyHomePage(self.driver).click_item_contacts_page()
        with (allure.step(f"2. Проверить, что определился ваш регион (г. Санкт-Петербург) и есть список партнеров")):
            saby_contacts_page = SabyContactsPage(self.driver)
            name_current_region = saby_contacts_page.get_name_current_region()
            assert name_current_region == Regions.spb_region, \
                f"Название текущего региона определяется некорректно"
            name_spb_partner = saby_contacts_page.get_name_spb_partner()
            assert name_spb_partner == Partners.spb_partner, \
                f"Блок 'Список партнеров' текущего региона не найден на странице"
        with allure.step(f"3. Изменить регион на Камчатский край"):
            saby_contacts_page.change_region_to_kamchatka()
        with allure.step(f"4. Проверить, что подставился выбранный регион, список партнеров изменился,"
                         f"url и title содержат информацию выбранного региона"):
            name_current_region = saby_contacts_page.get_name_current_region()
            assert name_current_region == Regions.kamchatka_region, \
                f"Название текущего региона определяется некорректно"
            name_kamchatka_partner = saby_contacts_page.get_name_kamchatka_partner()
            assert name_kamchatka_partner == Partners.kamchatka_partner, \
                f"Блок 'Список партнеров' текущего региона не найден на странице"
            current_url = saby_contacts_page.get_current_url()
            assert TestDataSaby.URL_CONTACTS_KAMCHATKA in current_url, \
                f"Текущий URL не соответствует URL выбранного региона"
            current_title = saby_contacts_page.get_page_title()
            assert current_title == SabyTitles.kamchatka_title, \
                f"Название заголовка текущей страницы сайта не соответствует ожидаемому"

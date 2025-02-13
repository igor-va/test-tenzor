import pytest
import allure
import time

from pages.saby.saby_home_page import SabyHomePage
from pages.saby.saby_contacts_page import SabyContactsPage
from pages.tensor.tensor_home_page import TensorHomePage
from configurations.test_data import *


@allure.feature("Тестовое задание")
@pytest.mark.ui
class TestOne:

    @allure.title("Первый сценарий")
    @allure.description("Первый сценарий тестового задания")
    @pytest.mark.tc1
    def test_one(self, fixture_setup) -> None:
        """Первый сценарий тестового задания"""
        self.driver = fixture_setup
        with allure.step(f"1. Перейти на https://sbis.ru/ в раздел 'Контакты'"):
            self.driver.get(TestDataSaby.URL)
            SabyHomePage(self.driver).click_item_contacts()
        with allure.step(f"2. Найти баннер 'Тензор', кликнуть по нему"):
            SabyContactsPage(self.driver).click_item_tensor_logo()
        with allure.step(f"3. Перейти на https://tensor.ru/"):
            tabs = self.driver.window_handles
            self.driver.switch_to.window(tabs[1])
        with allure.step(f"4. Проверить, что есть блок 'Сила в людях'"):
            assert TensorHomePage(self.driver).verify_block_people_power(), \
                f"Блок 'Сила в людях' не найден на странице {self.driver.current_url}"



            time.sleep(5)

            # page_title = home_page.get_page_title()
            # assert Titles.catalog_title in page_title, Titles.error_title


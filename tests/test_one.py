import pytest
import allure
import time

from pages.saby.saby_home_page import SabyHomePage
from pages.saby.saby_contacts_page import SabyContactsPage
from pages.tensor.tensor_home_page import TensorHomePage
from configurations.test_data import *


@allure.feature("Тестовое задание")
@pytest.mark.ui
class TestClass:

    @allure.title("Первый сценарий")
    @allure.description("Первый сценарий тестового задания")
    @pytest.mark.tc1
    def test_one(self, fixture_setup) -> None:
        """Первый сценарий тестового задания"""
        self.driver = fixture_setup
        with allure.step(f"1. Перейти на https://sbis.ru/ в раздел 'Контакты'"):
            self.driver.get(TestDataSaby.URL_HOME)
            SabyHomePage(self.driver).click_item_contacts()
        with allure.step(f"2. Найти баннер 'Тензор', кликнуть по нему"):
            SabyContactsPage(self.driver).click_item_tensor_logo()
        with allure.step(f"3. Перейти на https://tensor.ru/"):
            tabs = self.driver.window_handles
            self.driver.switch_to.window(tabs[1])
        with allure.step(f"4. Проверить, что есть блок 'Сила в людях'"):
            tensor_home_page = TensorHomePage(self.driver)
            assert tensor_home_page.verify_block_people_power_displayed(), \
                f"Блок 'Сила в людях' не найден на странице {self.driver.current_url}"
        with allure.step(f"5. Перейдите в этом блоке в 'Подробнее' и убедитесь, что откроется https://tensor.ru/about"):
            tensor_home_page.click_item_block_people_power_about()
            current_url = tensor_home_page.get_current_url()
            assert current_url == TestDataTensor.URL_ABOUT
        with allure.step(f"6. Находим раздел 'Работаем' и проверяем, что у всех фотографии хронологии \
                        одинаковые высота (height) и ширина (width)"):



            time.sleep(3)

            # page_title = home_page.get_page_title()
            # assert Titles.catalog_title in page_title, Titles.error_title


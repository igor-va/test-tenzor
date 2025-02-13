import pytest
import allure
import time

from pages.base_page import BasePage
from pages.saby.saby_home_page import SabyHomePage
from pages.saby.saby_contacts_page import SabyContactsPage
from pages.tensor.tensor_home_page import TensorHomePage
from configurations.test_data import *
# from Info.Titles import Titles


@allure.feature("Тестовое задание")
@pytest.mark.ui
class TestOne:

    @allure.title("Первый сценарий")
    @allure.description("Первый сценарий тестового задания")
    @pytest.mark.tc1
    def test_one(self, fixture_setup) -> None:
        """Первый сценарий тестового задания"""
        self.driver = fixture_setup
        with allure.step(f"Перейти на https://sbis.ru/ в раздел 'Контакты'"):
            self.driver.get(TestDataSaby.URL)
            SabyHomePage(self.driver).click_item_contacts()
        with allure.step(f"Найти баннер 'Тензор', кликнуть по нему"):
            SabyContactsPage(self.driver).click_item_tensor_logo()
        with allure.step(f"Перейти на https://tensor.ru/"):
            # tabs = self.driver.window_handles
            # self.driver.switch_to.window(tabs[1])

            TensorHomePage(self.driver).wait_load_tensor_banner()
            current_url = self.driver.current_url
            assert current_url == TestDataTensor.URL, \
                f"Текущий 'URL' должен быть {TestDataTensor.URL}, но получен {current_url}"

            time.sleep(5)

            # page_title = home_page.get_page_title()
            # assert Titles.catalog_title in page_title, Titles.error_title


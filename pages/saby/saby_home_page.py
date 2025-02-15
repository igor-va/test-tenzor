from ..base_page import BasePage
from locators.saby.saby_home_locators import SabyHomeLocators


class SabyHomePage(BasePage):
    """Класс для хранений действий на сайте 'Saby' страницы 'Домашняя"""

    def __init__(self, driver):
        super().__init__(driver)

    def click_item_contacts_page(self) -> None:
        """Переход на страницу 'Контакты'"""
        BasePage.action_click(self, element=SabyHomeLocators.loc_contacts_head_preview)
        BasePage.action_click(self, element=SabyHomeLocators.loc_contacts_head)

    def click_item_footer_download_page(self) -> None:
        """Переход на страницу 'Скачать'"""
        BasePage.action_click(self, element=SabyHomeLocators.loc_download)

from ..base_page import BasePage
from locators.saby.saby_home_locators import SabyHomeLocators


class SabyHomePage(BasePage):
    """Класс для хранений действий на сайте 'Saby' страницы 'SabyHomePage"""

    def __init__(self, driver):
        super().__init__(driver)

    def click_item_contacts(self) -> None:
        """Переход на страницу 'Контакты"""
        BasePage.action_click(self, element=SabyHomeLocators.loc_contacts_head_preview)
        BasePage.action_click(self, element=SabyHomeLocators.loc_contacts_head)

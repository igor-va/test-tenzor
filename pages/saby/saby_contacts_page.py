from ..base_page import BasePage
from locators.saby.saby_contacts_locators import SabyContactsLocators


class SabyContactsPage(BasePage):
    """Класс для хранений действий на сайте 'Saby' страницы 'SabyContactsPage"""

    def __init__(self, driver):
        super().__init__(driver)

    def click_item_tensor_logo(self) -> None:
        """Переход на сайт 'Tensor'"""
        BasePage.action_click(self, element=SabyContactsLocators.loc_tensor_logo)

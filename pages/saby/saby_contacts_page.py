from ..base_page import BasePage
from locators.saby.saby_contacts_locators import SabyContactsLocators


class SabyContactsPage(BasePage):
    """Класс для хранений действий на сайте 'Saby' страницы 'SabyContactsPage"""

    def __init__(self, driver):
        super().__init__(driver)

    def click_item_tensor_logo(self) -> None:
        """Переход на сайт 'Tensor'"""
        BasePage.action_click(self, element=SabyContactsLocators.loc_tensor_logo)

    def get_local_region(self) -> str:
        """Получение текста местного региона"""
        status_displayed = BasePage.element_status_displayed(self, element=SabyContactsLocators.loc_block_local_region)
        if status_displayed:
            text_element = BasePage.get_text_element(self, element=SabyContactsLocators.loc_block_local_region)
            return text_element
        else:
            return ""

    def verify_block_partners_displayed(self) -> bool:
        """Проверка отображения блока 'Список партнеров'"""
        return BasePage.element_status_displayed(self, element=SabyContactsLocators.loc_block_partners)

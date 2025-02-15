from ..base_page import BasePage
from locators.saby.saby_contacts_locators import SabyContactsLocators


class SabyContactsPage(BasePage):
    """Класс для хранений действий на сайте 'Saby' страницы 'SabyContactsPage"""

    def __init__(self, driver):
        super().__init__(driver)

    def click_item_tensor_logo(self) -> None:
        """Переход на сайт 'Tensor'"""
        BasePage.action_click(self, element=SabyContactsLocators.loc_tensor_logo)

    def get_name_local_region(self) -> str:
        """Получение названия местного региона"""
        status_displayed = BasePage.element_status_displayed(self, element=SabyContactsLocators.loc_block_region_chooser)
        if status_displayed:
            text_element = BasePage.get_text_element(self, element=SabyContactsLocators.loc_block_region_chooser)
            return text_element
        else:
            return ""

    def change_region_to_kamchatka(self) -> None:
        """Изменить регион на Камчатский край"""
        BasePage.action_click(self, element=SabyContactsLocators.loc_block_region_chooser)
        BasePage.action_click(self, element=SabyContactsLocators.loc_block_region_kamchatka)

    def get_name_local_partner(self) -> str:
        """Получение названия местного партнера"""
        text_element = BasePage.get_text_element(self, element=SabyContactsLocators.loc_block_partners)
        return text_element

from ..base_page import BasePage
from locators.saby.saby_contacts_locators import SabyContactsLocators


class SabyContactsPage(BasePage):
    """Класс для хранений действий на сайте 'Saby' страницы 'Контакты"""

    def __init__(self, driver):
        super().__init__(driver)

    def click_item_tensor_logo(self) -> None:
        """Переход на сайт 'Tensor'"""
        BasePage.action_click(self, element=SabyContactsLocators.loc_tensor_logo)

    def get_name_current_region(self) -> str:
        """Получение названия текущего региона"""
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

    def get_name_spb_partner(self) -> str:
        """Получение названия партнера в Санкт-Петербурге"""
        text_element = BasePage.get_text_element(self, element=SabyContactsLocators.loc_block_spb_partner)
        return text_element

    def get_name_kamchatka_partner(self) -> str:
        """Получение названия партнера в Камчатском Крае"""
        text_element = BasePage.get_text_element(self, element=SabyContactsLocators.loc_block_kamchatka_partner)
        return text_element

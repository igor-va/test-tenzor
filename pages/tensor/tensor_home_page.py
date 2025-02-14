from ..base_page import BasePage
from locators.tensor.tensor_home_locators import TensorHomeLocators


class TensorHomePage(BasePage):
    """Класс для хранений действий на сайте 'Tensor' страницы 'TensorHomePage"""

    def __init__(self, driver):
        super().__init__(driver)

    def verify_block_people_power_displayed(self) -> bool:
        """Проверка отображения блока 'Сила в людях'"""
        return BasePage.element_status_displayed(self, element=TensorHomeLocators.loc_block_people_power)

    def click_item_block_people_power_about(self) -> None:
        """Переход на страницу 'О компании"""
        BasePage.action_click(self, element=TensorHomeLocators.loc_block_people_power_about)

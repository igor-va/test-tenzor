from ..base_page import BasePage
from locators.tensor.tensor_about_locators import TensorAboutLocators


class TensorAboutPage(BasePage):
    """Класс для хранений действий на сайте 'Tensor' страницы 'TensorAboutPage"""

    def __init__(self, driver):
        super().__init__(driver)

    def verify_block_people_power_displayed(self):
        return BasePage.element_status_displayed(self, element=TensorAboutLocators.loc_block_people_power)



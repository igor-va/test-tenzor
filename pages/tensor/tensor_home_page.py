from ..base_page import BasePage
from locators.tensor.tensor_home_locators import TensorHomeLocators


class TensorHomePage(BasePage):

    def __init__(self, driver):
        super().__init__(driver)

    def verify_block_people_power(self):
        return BasePage.element_status_displayed(self, element=TensorHomeLocators.loc_block_people_power)



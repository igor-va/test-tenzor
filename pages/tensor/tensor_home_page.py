from ..base_page import BasePage
from locators.tensor.tensor_home_locators import TensorHomeLocators


class TensorHomePage(BasePage):

    def __init__(self, driver):
        super().__init__(driver)

    def wait_load_tensor_banner(self):
        BasePage.wait_load_element(self, element=TensorHomeLocators.loc_tensor_banner)



from ..base_page import BasePage
from locators.tensor.tensor_about_locators import TensorAboutLocators


class TensorAboutPage(BasePage):
    """Класс для хранений действий на сайте 'Tensor' страницы 'TensorAboutPage"""

    def __init__(self, driver):
        super().__init__(driver)

    def verify_block_work_images_same_size(self) -> bool:
        """Проверка, что все фотографии в разделе 'Работаем' имеют одинаковые размеры"""

        all_sizes = []
        elements = BasePage.get_all_elements(self, element=TensorAboutLocators.loc_block_work_images)
        for element in elements:
            element_size = element.size
            all_sizes.append((element_size['height'], element_size['width']))
        if len(set(all_sizes)) == 1:
            return True
        else:
            return False

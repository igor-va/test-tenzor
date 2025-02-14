from selenium.webdriver.common.by import By


class TensorAboutLocators:
    """Локаторы для сайта 'Tensor' страницы 'TensorAboutPage'"""

    loc_block_work_images = (By.XPATH, "//img[contains(@class, 'tensor_ru-About__block3-image')]")

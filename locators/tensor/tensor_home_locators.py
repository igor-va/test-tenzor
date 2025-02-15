from selenium.webdriver.common.by import By


class TensorHomeLocators:
    """Локаторы для сайта 'Tensor' страницы 'Домашняя'"""

    loc_block_people_power = (By.XPATH, "//p[contains(text(), 'Сила в людях')]")
    loc_block_people_power_about = (By.XPATH, "//div[@class='tensor_ru-Index__block4-bg']//a[contains(text(), 'Подробнее')]")

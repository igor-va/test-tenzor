from selenium.webdriver.common.by import By


class SabyContactsLocators:
    """Локаторы для сайта 'Saby' страницы 'SabyContactsPage'"""

    # Сайт Tensor
    loc_tensor_logo = (By.XPATH, "//div[@id='contacts_clients']//a[@title='tensor.ru']")

    # Регионы
    loc_block_region_chooser = [By.XPATH, "//span[contains(@class, 'Region-Chooser')]"]
    loc_block_region_kamchatka = [By.XPATH, "//span[contains(text(), '41 Камчатский край')]"]

    # Партнеры
    loc_block_spb_partner = (By.XPATH, "//div[contains(text(), 'Saby - Санкт-Петербург')]")
    loc_block_kamchatka_partner = (By.XPATH, "//div[contains(text(), 'Saby - Камчатка')]")

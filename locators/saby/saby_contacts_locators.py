from selenium.webdriver.common.by import By


class SabyContactsLocators:
    """Локаторы для сайта 'Saby' страницы 'SabyContactsPage'"""

    loc_tensor_logo = (By.XPATH, "//div[@id='contacts_clients']//a[@title='tensor.ru']")
    loc_block_local_region = (By.XPATH, "//span[@class='sbis_ru-Region-Chooser__text sbis_ru-link']")
    loc_block_partners = (By.XPATH, "//div[contains(text(), 'Saby - Санкт-Петербург')]")

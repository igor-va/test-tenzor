from selenium.webdriver.common.by import By


class SabyContactsLocators:
    """Локаторы для сайта 'Saby' страницы 'SabyContactsPage'"""

    loc_tensor_logo = (By.XPATH, "//div[@id='contacts_clients']//a[@title='tensor.ru']")

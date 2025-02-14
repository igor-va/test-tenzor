from selenium.webdriver.common.by import By


class BaseLocators:
    """Локаторы для страницы 'BasePage'"""

    loc_obscure_preload = (By.XPATH, "//div[@class='preload-overlay']")

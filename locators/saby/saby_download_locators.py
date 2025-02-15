from selenium.webdriver.common.by import By


class SabyDownloadLocators:
    """Локаторы для сайта 'Saby' страницы 'Скачать'"""

    # Saby Plugin
    # loc_plugin_web_installer = (By.LINK_TEXT, "Скачать (Exe 10.42 МБ) ")
    loc_plugin_web_installer = (By.XPATH, "//a[contains(text(), 'Скачать (Exe 10.42 МБ)')]")

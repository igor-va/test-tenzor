from selenium.webdriver.common.by import By


class SabyHomeLocators:
    """Локаторы для сайта 'Saby' страницы 'Домашняя'"""

    # Страница 'Контакты'
    loc_contacts_head_preview = (By.XPATH, "//div[contains(text(), 'Контакты')]")
    loc_contacts_head = (By.PARTIAL_LINK_TEXT, 'Еще')

    # Страница 'Скачать'
    loc_download = (By.LINK_TEXT, 'Скачать локальные версии')

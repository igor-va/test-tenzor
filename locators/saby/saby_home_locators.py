from selenium.webdriver.common.by import By


class SabyHomeLocators:
    """Локаторы для сайта 'Saby' страницы 'SabyHomePage'"""

    loc_contacts_head = (By.LINK_TEXT, "Еще 25 офисов в регионе")
    loc_contacts_head_preview = (By.XPATH, "//div[contains(text(), 'Контакты')]")

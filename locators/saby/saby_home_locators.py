from selenium.webdriver.common.by import By


class SabyHomeLocators:
    loc_contacts_head_preview = (By.XPATH, "//div[contains(text(), 'Контакты')]")
    loc_contacts_head = (By.LINK_TEXT, "Еще 25 офисов в регионе")



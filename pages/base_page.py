from selenium.webdriver.support import expected_conditions as ec
from selenium.webdriver.support.wait import WebDriverWait
from locators.base_locators import BaseLocators


class BasePage:
    """Базовый класс общих действий пользователя на странице"""

    def __init__(self, driver):
        self.driver = driver
        self.timeout = 30

    def action_text_clear(self, element) -> None:
        """Очистка текста в поле ввода"""
        WebDriverWait(self.driver, self.timeout).until(ec.visibility_of_element_located(element)).clear()

    def action_text_type(self, element, text) -> None:
        """Ввод текста в поле ввода"""
        WebDriverWait(self.driver, self.timeout).until(ec.visibility_of_element_located(element)).send_keys(text)

    def action_click(self, element) -> None:
        """Нажатие на элемент"""
        WebDriverWait(self.driver, self.timeout).until(ec.invisibility_of_element_located(BaseLocators.loc_obscure_preload))
        WebDriverWait(self.driver, self.timeout).until(ec.visibility_of_element_located(element)).click()

    def get_text_element(self, element) -> str:
        """Получение текст элемента"""
        return WebDriverWait(self.driver, self.timeout).until(ec.visibility_of_element_located(element)).text

    def element_status_enabled(self, element) -> bool:
        """Проверка присутствия элемента на странице"""
        return WebDriverWait(self.driver, self.timeout).until(ec.visibility_of_element_located(element)).is_enabled()

    def element_status_displayed(self, element) -> bool:
        """Проверка отображения элемента на странице"""
        return WebDriverWait(self.driver, self.timeout).until(ec.visibility_of_element_located(element)).is_displayed()

    def get_page_title(self) -> str:
        """Получение названия текущей страницы"""
        return self.driver.title

    def get_current_url(self) -> str:
        """Получение URL текущей страницы"""
        return self.driver.current_url


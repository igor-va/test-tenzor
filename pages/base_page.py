from selenium.webdriver.support import expected_conditions as ec
from selenium.webdriver.support.wait import WebDriverWait
from locators.base_locators import BaseLocators


class BasePage:
    """Базовый класс общих действий на странице"""

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
        text_element = WebDriverWait(self.driver, self.timeout).until(ec.visibility_of_element_located(element)).text
        return text_element

    def element_status_enabled(self, element) -> bool:
        """Проверка присутствия элемента на странице"""
        status = WebDriverWait(self.driver, self.timeout).until(ec.visibility_of_element_located(element)).is_enabled()
        return status

    def element_status_displayed(self, element) -> bool:
        """Проверка отображения элемента на странице"""
        status = WebDriverWait(self.driver, self.timeout).until(ec.visibility_of_element_located(element)).is_displayed()
        return status

    def get_all_elements(self, element):
        """Получение всех подходящих элементов"""
        all_elements = WebDriverWait(self.driver, self.timeout).until(ec.visibility_of_all_elements_located(element))
        return all_elements

    def get_page_title(self) -> str:
        """Получение названия текущей страницы"""
        return self.driver.title

    def get_current_url(self) -> str:
        """Получение URL текущей страницы"""
        return self.driver.current_url

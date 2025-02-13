from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver import ActionChains
from locators.base_locators import BaseLocators


class BasePage:

    def __init__(self, driver):
        self.driver = driver
        self.timeout = 30

    def action_text_clear(self, element):
        WebDriverWait(self.driver, self.timeout).until(EC.visibility_of_element_located(element)).clear()

    def action_text_type(self, element, text):
        WebDriverWait(self.driver, self.timeout).until(EC.visibility_of_element_located(element)).send_keys(text)

    def action_click(self, element):
        WebDriverWait(self.driver, self.timeout).until(EC.invisibility_of_element_located(BaseLocators.loc_obscure_preload))
        WebDriverWait(self.driver, self.timeout).until(EC.visibility_of_element_located(element)).click()

    def get_text_element(self, element):
        return WebDriverWait(self.driver, self.timeout).until(EC.visibility_of_element_located(element)).text

    def element_status_enabled(self, element):
        return WebDriverWait(self.driver, self.timeout).until(EC.visibility_of_element_located(element)).is_enabled()

    def element_status_displayed(self, element):
        return WebDriverWait(self.driver, self.timeout).until(EC.visibility_of_element_located(element)).is_displayed()

    def scroll_to_element_tag(self, element):
        pass
        # element = WebDriverWait(self.driver, self.timeout).until(EC.visibility_of_element_located(element))
        # ActionChains(self.driver).scroll_to_element(element).perform()

    def wait_load_element(self, element):
        WebDriverWait(self.driver, self.timeout).until(EC.presence_of_element_located(element)).is_displayed()

    def get_page_title(self):
        return self.driver.title

    def get_current_url(self, tab):
        self.driver.switch_to.window(tab)
        return self.driver.current_url



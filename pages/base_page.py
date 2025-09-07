import allure
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait


class BasePage:
    def __init__(self, driver):
        self.driver = driver

    @allure.step('Открытие страницы {url}')
    def open_page(self, url):  
        return self.driver.get(url)

    @allure.step('Прокрутка к нужному элементу')
    def scroll_to_element(self, locator):  
        element = self.driver.find_element(*locator)
        self.driver.execute_script("arguments[0].scrollIntoView();", element)

    @allure.step('Ожидание видимости элемента')
    def wait_for_visibility(self, locator, timeout=7):  
        WebDriverWait(self.driver, timeout).until(expected_conditions.visibility_of_element_located(locator))

    @allure.step('Ожидание кликабельности элемента')
    def wait_for_clickability(self, locator, timeout=7):  
        WebDriverWait(self.driver, timeout).until(expected_conditions.element_to_be_clickable(locator))

    @allure.step('Получение текстового значения из элемента')
    def get_text(self, locator):  
        return self.driver.find_element(*locator).text

    @allure.step('Получение значения элемента')
    def get_value(self, locator, value):  
        return self.driver.find_element(*locator).get_attribute(value)

    @allure.step('Перемещение элемента способом Drag and drop')
    def replace_element(self, element_locator, place_locator):
        action_chains = ActionChains(self.driver)
        return action_chains.drag_and_drop(element_locator, place_locator).perform()
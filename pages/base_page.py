import allure
import urls
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait
from locators.build_burger_locators import BurgerLocators as bl


class BasePage:
    def __init__(self, driver):
        self.driver = driver

    @allure.step('Вход в аккаунт')
    def auth(self, create_user):
        email, password = create_user

        self.open_page(urls.LOGIN_USER)
        self.enter_text(*bl.EMAIL_FIELD_FOR_AUTH, text=email)
        self.enter_text(*bl.PASSWORD_AUTH_FIELD, text=password)
        self.click_element(*bl.LOGIN_BUTTON)

    @allure.step('Открытие страницы {url}')
    def open_page(self, url):  
        return self.driver.get(url)
    
    @allure.step('Найти элемент')
    def find_element(self, *locator):
        return self.driver.find_element(*locator)
    
    @allure.step('Кликнуть на элементе')
    def click_element(self, *locator):
        element = WebDriverWait(self.driver, 7).until(EC.presence_of_element_located(locator))
        element.click()

    @allure.step('Кликнуть на элементе с помощью JavaScript')
    def click_JS_element(self, element): 
        self.driver.execute_script("arguments[0].click();", element)    

    @allure.step('Ввести значение в поле для ввода')
    def enter_text(self, *locator, text):
        element = self.wait_for_visibility(locator)
        element.send_keys(text)    

    @allure.step('Прокрутка к нужному элементу')
    def scroll_to_element(self, *locator):  
        element = self.driver.find_element(*locator)
        self.driver.execute_script("arguments[0].scrollIntoView();", element)

    @allure.step('Ожидание видимости элемента')
    def wait_for_visibility(self, locator, timeout=7):  
        return WebDriverWait(self.driver, timeout).until(EC.visibility_of_element_located(locator))

    @allure.step('Ожидание кликабельности элемента')
    def wait_for_clickability(self, locator, timeout=7):  
        WebDriverWait(self.driver, timeout).until(EC.element_to_be_clickable(locator))

    @allure.step('Получение текстового значения из элемента')
    def get_text_from_element(self, *locator):
        return self.driver.find_element(*locator).text
    
    @allure.step('Получение значения элемента')
    def get_value(self, *locator, value):  
        return self.driver.find_element(*locator).get_attribute(value)
    
    @allure.step('Получение url')
    def get_url(self):
        return self.driver.current_url
    
    @allure.step('Проверка отображения элемента')
    def element_displayed(self, *locator):
        return self.wait_for_visibility(locator).is_displayed()

    @allure.step('Перемещение элемента способом Drag and drop')
    def drag_n_drop_element(self, element_locator, place_locator):
        ActionChains(self.driver).drag_and_drop(element_locator, place_locator).perform()
    
    @allure.step('Ожидание счетчика ингредиента')
    def wait_ingredient_counter(self):
        try:
            WebDriverWait(self.driver, 7).until(lambda d: int(self.get_text_from_element(*bl.INGREDIENT_COUNTER)) > 0)
        except (ValueError, Exception):
            # If counter element doesn't exist or has invalid value, wait for it to appear
            WebDriverWait(self.driver, 7).until(EC.presence_of_element_located(bl.INGREDIENT_COUNTER))
    
    @allure.step('Ожидание пока номер заказа станет отличным от 9999')
    def wait_order_number_change(self):        
        WebDriverWait(self.driver, 7).until(lambda d: self.get_text_from_element(*bl.ORDER_NUMBER) != '9999')      
import allure
from locators import build_burger_locators as loc
from pages.base_page import BasePage
from selenium.webdriver.support.wait import WebDriverWait


class BuildBurgerPage(BasePage):

    @allure.step('Кликнуть на кнопку "Конструктор"')
    def click_constructor(self):
        self.driver.find_element(*loc.CONSTRUCTOR_BUTTON).click()

    @allure.step('Кликнуть на кнопку "Лента заказов"')
    def click_feed_button(self):
        try:
            self.wait_for_clickability(loc.ORDER_LIST_BUTTON, 7)
            self.driver.find_element(*loc.ORDER_LIST_BUTTON).click()
        except Exception:
            # Fallback to JS click if element is intercepted
            feed_btn = self.driver.find_element(*loc.ORDER_LIST_BUTTON)
            self.driver.execute_script("arguments[0].click();", feed_btn)

    @allure.step('Кликнуть на ингредиент')
    def click_ingredient(self):
        self.driver.find_element(*loc.INGREDIENT).click()

    @allure.step('Свернуть окно ингредиента (нажать на крестик)')
    def minimize_ingredient_popup(self):
        self.driver.find_element(*loc.CLOSE_DETAILS_POPUP).click()

    @allure.step('Добавить ингредиент в заказ')
    def add_ingredient_to_order(self, locator):
        ingredient = self.driver.find_element(*locator)
        order_area = self.driver.find_element(*loc.ORDER_SECTION)
        self.replace_element(ingredient, order_area)

    @allure.step('Нажать "Оформить заказ"')
    def click_make_order_button(self):
        self.driver.find_element(*loc.MAKE_ORDER_BUTTON).click()

    @allure.step('Сделать заказ')
    def make_order(self, locator):
        self.add_ingredient_to_order(locator)
        self.click_make_order_button()
        self.wait_for_clickability(loc.MAKE_ORDER_BUTTON, 7)

    @allure.step('Свернуть окно заказа (нажать на крестик)')
    def minimize_order_popup(self):
        # Убедиться, что кнопка закрытия присутствует и кликабельна, затем нажать на неё
        try:
            self.wait_for_visibility(loc.CONFIRMATION_POPUP, 7)
            self.wait_for_clickability(loc.CLOSE_ORDER_POPUP, 7)
            self.driver.find_element(*loc.CLOSE_ORDER_POPUP).click()
        except Exception:
            close_btn = self.driver.find_element(*loc.CLOSE_ORDER_POPUP)
            self.driver.execute_script("arguments[0].click();", close_btn)
        
        # Small wait for modal to close
        import time
        time.sleep(1)

    @allure.step('Ожидание пока номер заказа станет отличным от 9999')
    def wait_order_number(self):        
        WebDriverWait(self.driver, 7).until(lambda d: self.get_text(loc.ORDER_NUMBER) != '9999')
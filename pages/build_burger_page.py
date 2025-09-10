import allure
from locators.build_burger_locators import BurgerLocators as bl
from pages.base_page import BasePage


class BuildBurgerPage(BasePage):

    @allure.step('Кликнуть на кнопку "Конструктор"')
    def click_constructor(self):
        self.wait_for_visibility(bl.CONSTRUCTOR_BUTTON)
        self.click_element(*bl.CONSTRUCTOR_BUTTON)

    @allure.step('Кликнуть на кнопку "Лента заказов"')
    def click_feed_button(self):
        feed_button = self.find_element(*bl.ORDER_LIST_BUTTON)
        self.click_JS_element(feed_button)
     
    @allure.step('Кликнуть на ингредиент')
    def click_ingredient(self):
        self.click_element(*bl.INGREDIENT)

    @allure.step('Открытие карточки ингредиента')
    def display_ingredient_info(self):
        return self.element_displayed(*bl.BUN_INFO)    

    @allure.step('Свернуть окно ингредиента (нажать на крестик)')
    def minimize_ingredient_popup(self):
        self.wait_for_clickability(bl.CLOSE_DETAILS_POPUP)
        self.click_element(*bl.CLOSE_DETAILS_POPUP)   

    @allure.step('Свернуть окно заказа (нажать на крестик)')
    def minimize_order_popup(self):
        self.wait_for_visibility(bl.CONFIRMATION_POPUP)
        self.wait_for_clickability(bl.CLOSE_ORDER_POPUP)
        close_button = self.find_element(*bl.CLOSE_ORDER_POPUP)
        self.click_JS_element(close_button)   

    @allure.step('Проверить закрытие модального окна')
    def check_if_closed(self):
        return self.element_displayed(*bl.BUILD_BURGER)            

    @allure.step('Добавить ингредиент в заказ')
    def add_ingredient_to_order(self, locator):
        ingredient = self.find_element(*locator)
        order_area = self.find_element(*bl.ORDER_SECTION)
        self.drag_n_drop_element(ingredient, order_area)

    @allure.step('Добавить первый ингредиент в заказ')
    def add_first_ingredient_to_order(self):
        ingredient = self.find_element(*bl.INGREDIENT)
        order_area = self.find_element(*bl.ORDER_SECTION)
        self.drag_n_drop_element(ingredient, order_area)

    @allure.step('Получить значение счетчика ингредиента')
    def get_ingredient_counter_value(self):
        try:
            return int(self.get_text_from_element(*bl.INGREDIENT_COUNTER))
        except (ValueError, Exception):
            return 0

    @allure.step('Нажать "Оформить заказ"')
    def click_make_order_button(self):
        self.click_element(*bl.MAKE_ORDER_BUTTON)

    @allure.step('Сделать заказ')
    def make_order(self, locator):
        self.add_ingredient_to_order(locator)
        self.click_make_order_button()

    @allure.step('Сделать заказ с первым ингредиентом')
    def make_order_with_first_ingredient(self):
        self.add_first_ingredient_to_order()
        self.click_make_order_button()

    @allure.step('Ожидать кликабельности ингредиента')
    def wait_for_ingredient_clickability(self):
        self.wait_for_clickability(bl.INGREDIENT)

    @allure.step('Ожидать появления попапа подтверждения заказа')
    def wait_for_confirmation_popup(self):
        self.wait_for_visibility(bl.CONFIRMATION_POPUP)

    @allure.step('Проверить наличие попапа подтверждения заказа')
    def check_confirmation_popup_displayed(self):
        return self.element_displayed(*bl.CONFIRMATION_POPUP)
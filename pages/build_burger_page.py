import allure
from locators.build_burger_locators import BurgerLocators
from pages.base_page import BasePage


class BuildBurgerPage(BasePage):

    @allure.step('Кликнуть на кнопку "Конструктор"')
    def click_constructor(self):
        self.wait_for_visibility(BurgerLocators.CONSTRUCTOR_BUTTON)
        self.click_element(*BurgerLocators.CONSTRUCTOR_BUTTON)

    @allure.step('Кликнуть на кнопку "Лента заказов"')
    def click_feed_button(self):
        feed_button = self.find_element(*BurgerLocators.ORDER_LIST_BUTTON)
        self.driver.execute_script("arguments[0].click();", feed_button)
     
    @allure.step('Кликнуть на ингредиент')
    def click_ingredient(self):
        self.click_element(*BurgerLocators.INGREDIENT)

    @allure.step('Свернуть окно ингредиента (нажать на крестик)')
    def minimize_ingredient_popup(self):
        self.wait_for_clickability(BurgerLocators.CLOSE_DETAILS_POPUP)
        self.click_element(*BurgerLocators.CLOSE_DETAILS_POPUP)   

    @allure.step('Добавить ингредиент в заказ')
    def add_ingredient_to_order(self, locator):
        ingredient = self.find_element(*locator)
        order_area = self.find_element(*BurgerLocators.ORDER_SECTION)
        self.drag_n_drop_element(ingredient, order_area)

    @allure.step('Нажать "Оформить заказ"')
    def click_make_order_button(self):
        self.click_element(*BurgerLocators.MAKE_ORDER_BUTTON)

    @allure.step('Сделать заказ')
    def make_order(self, locator):
        self.add_ingredient_to_order(locator)
        self.click_make_order_button()
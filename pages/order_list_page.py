import allure
from locators import order_list_locators as loc
from pages.base_page import BasePage


class OrderListPage(BasePage):

    @allure.step('Нажать на заказ')
    def click_order(self):
        self.driver.find_element(*loc.ORDER_FROM_LIST).click()

    @allure.step('Закрыть окно заказа нажатием на крестик)')
    def close_order_popup(self):
        self.driver.find_element(*loc.CLOSE_ORDER_POPUP).click()
import allure
import urls
from locators import order_list_locators as loc
from pages.base_page import BasePage


class OrderListPage(BasePage):

    @allure.step('Вход в аккаунт')
    def auth(self, create_user):
        email, password = create_user

        self.open_page(urls.LOGIN_USER)
        self.enter_text(*loc.EMAIL_FIELD_FOR_AUTH, text=email)
        self.enter_text(*loc.PASSWORD_AUTH_FIELD, text=password)
        self.click_element(*loc.LOGIN_BUTTON)
    
    @allure.step('Кликнуть на кнопку "Конструктор"')
    def click_constructor(self):
        self.wait_for_visibility(loc.CONSTRUCTOR_BUTTON)
        self.click_element(*loc.CONSTRUCTOR_BUTTON)

    @allure.step('Нажать "Оформить заказ"')
    def click_make_order_button(self):
        self.click_element(*loc.MAKE_ORDER_BUTTON)

    @allure.step('Получить номер заказа сразу после оформления')
    def order_number_in_text(self):
        self.wait_for_visibility(loc.ORDER_NUMBER)
        return self.get_text_from_element(*loc.ORDER_NUMBER)        
    
    @allure.step('Нажать на заказ')
    def click_order(self):
        self.click_element(*loc.ORDER_FROM_LIST)

    @allure.step('Проверить на странице наличие окна заказа')
    def check_order_info_displayed(self):
        return self.element_displayed(*loc.ORDER_POPUP)        

    @allure.step('Получить номер заказа в статусе "В работе"')
    def order_number_in_progress(self):
        self.wait_for_clickability(loc.ORDER_NUMBER_IN_PROGRESS)
        return self.get_text_from_element(*loc.ORDER_NUMBER_IN_PROGRESS)   

    @allure.step('Получить номер заказа из истории')
    def text_order_number_from_history(self):
        self.wait_for_clickability(loc.ORDER_NUMBER_IN_HISTORY)
        return self.get_text_from_element(*loc.ORDER_NUMBER_IN_HISTORY) 
    
    @allure.step('Получить количество заказов за сегодня')
    def text_total_orders_for_today(self):
        self.wait_for_clickability(loc.DONE_TODAY)
        return self.get_text_from_element(*loc.DONE_TODAY)
    
    @allure.step('Получить количество заказов за всё время')
    def text_order_all_time(self):
        self.wait_for_clickability(loc.DONE_ALL_TIME)
        return self.get_text_from_element(*loc.DONE_ALL_TIME)
    
    @allure.step('Клик по кнопке «Лента заказов»')
    def click_button_order_list(self):
        self.wait_for_visibility(loc.ORDER_LIST_BUTTON)
        self.click_element(*loc.ORDER_LIST_BUTTON)

    @allure.step('Нажатие кнопки «История заказов»')
    def click_on_order_history(self):
        self.wait_for_clickability(loc.ORDER_HISTORY_BUTTON)
        self.click_element(*loc.ORDER_HISTORY_BUTTON)    

    @allure.step('Закрыть окно заказа нажатием на крестик)')
    def close_order_popup(self):
        self.wait_for_clickability(loc.CLOSE_ORDER_POPUP)
        self.click_element(*loc.CLOSE_ORDER_POPUP)
    
    @allure.step('Получить номер заказа из ленты заказов')
    def text_feed_order_number(self):
        self.wait_for_clickability(loc.ORDER_NUMBER_IN_PROGRESS)
        return self.get_text_from_element(*loc.ORDER_NUMBER_IN_PROGRESS)   
    
    @allure.step('Перетащить ингредиент в конструктор')
    def drag_and_drop_ingredient_to_burger_side(self):
        element_locator = self.find_element(*loc.BUN)
        place_locator = self.find_element(*loc.BURGER_SIDE)
        self.drag_n_drop_element(element_locator, place_locator)

    @allure.step("Ожидание видимости текста в модальном окне")
    def wait_until_text_is_visible(self):
        self.wait_for_visibility(loc.MODAL_ORDER_IN_PROCESSING) 

    @allure.step('Нажатие на кнопку "Личный кабинет"')
    def click_user_account(self):
        self.wait_for_clickability(loc.USER_ACCOUNT_BUTTON)
        self.click_element(*loc.USER_ACCOUNT_BUTTON)       
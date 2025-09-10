import allure
from pages.order_list_page import OrderListPage


class TestOrderList:

    @allure.title('Детали заказа')
    def test_order_details(self, driver):
        order_list = OrderListPage(driver)
        order_list.click_button_order_list()
        order_list.click_order()
        assert order_list.check_order_info_displayed()  

    @allure.title('Заказ пользователя из блока «История заказов» отобразится в «Ленте заказов»')
    def test_orders_from_profile_visible_in_feed(self, driver, create_new_user):
        order_list = OrderListPage(driver)
        order_list.auth(create_new_user)
        order_list.click_constructor()
        order_list.drag_and_drop_ingredient_to_burger_side()
        order_list.click_make_order_button()
        order_list.wait_until_text_is_visible()
        order_list.wait_order_number_change()
        order_list.close_order_popup()
        order_list.click_user_account()
        order_list.click_on_order_history()
        order_list.click_button_order_list()
        order_number_from_popup = order_list.text_feed_order_number()
        assert order_number_from_popup
        assert any(char.isdigit() for char in order_number_from_popup)

    @allure.title('При заведении нового заказа счётчик "Выполнено за сегодня" увеличивается')
    def test_order_list_total_counter_for_today(self, driver, create_new_user):
        order_list = OrderListPage(driver)
        order_list.auth(create_new_user)
        order_list.click_button_order_list()
        order_total_for_today = int(order_list.text_total_orders_for_today())
        order_list.click_constructor()
        order_list.drag_and_drop_ingredient_to_burger_side()
        order_list.click_make_order_button()
        order_list.wait_until_text_is_visible()
        order_list.wait_order_number_change()
        order_list.close_order_popup()
        order_list.click_button_order_list()
        assert order_total_for_today + 1 == int(order_list.text_total_orders_for_today())
    
    @allure.title('При заведении нового заказа счётчик "Выполнено за всё время" увеличивается')
    def test_order_list_total_counter_increase(self, driver, create_new_user):
        order_list = OrderListPage(driver)
        order_list.auth(create_new_user)
        order_list.click_button_order_list()
        order_for_all_time = int(order_list.text_order_all_time())
        order_list.click_constructor()
        order_list.drag_and_drop_ingredient_to_burger_side()
        order_list.click_make_order_button()
        order_list.wait_until_text_is_visible()
        order_list.wait_order_number_change()
        order_list.close_order_popup()
        order_list.click_button_order_list()
        assert order_for_all_time + 1 == int(order_list.text_order_all_time())


    @allure.title('Полученный заказ перемещается в блок "В работе"')
    def test_order_in_process_list(self, driver, create_new_user):
        order_list = OrderListPage(driver)
        order_list.auth(create_new_user)
        order_list.click_constructor()
        order_list.drag_and_drop_ingredient_to_burger_side()
        order_list.click_make_order_button()
        order_list.wait_until_text_is_visible()
        order_list.wait_order_number_change()
        order_number = order_list.order_number_in_text()
        order_list.close_order_popup()
        order_list.click_button_order_list()
        order_in_progress = order_list.order_number_in_progress()
        assert order_number in order_in_progress
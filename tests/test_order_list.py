import allure

import urls
from locators import order_list_locators as ol_loc
from locators.build_burger_locators import BurgerLocators
from pages.order_list_page import OrderListPage
from pages.build_burger_page import BuildBurgerPage
from pages.user_account_page import UserAccountPage



class TestOrderList:

    @allure.title('Детали заказа')
    def test_order_details(self, driver):
        order_list = OrderListPage(driver)
        order_list.open_page(urls.ORDER_LIST)
        order_list.wait_for_clickability(ol_loc.ORDER_FROM_LIST)
        order_list.click_order()
        assert order_list.find_element(*ol_loc.ORDER_POPUP)

    @allure.title('Заказ пользователя из блока «История заказов» отобразится в «Ленте заказов»')
    def test_orders_from_profile_visible_in_feed(self, driver, create_new_user):
        order_list = OrderListPage(driver)
        user_page = UserAccountPage(driver)
        build_page = BuildBurgerPage(driver)

        user_page.open_page(urls.BASE_URL)
        user_page.auth(create_new_user)
        
        build_page.wait_for_clickability(BurgerLocators.INGREDIENT)
        build_page.make_order(BurgerLocators.INGREDIENT)
        build_page.wait_for_visibility(BurgerLocators.CONFIRMATION_POPUP)
        
        order_number_from_popup = build_page.get_text_from_element(*BurgerLocators.ORDER_NUMBER)
        assert order_number_from_popup, "Номер заказа не может быть пустым"
        assert any(char.isdigit() for char in order_number_from_popup)

    @allure.title('При заведении нового заказа счётчик "Выполнено за сегодня" увеличивается')
    def test_order_list_total_counter_for_today(self, driver, create_new_user):
        order_list = OrderListPage(driver)
        user_page = UserAccountPage(driver)
        build_page = BuildBurgerPage(driver)

        user_page.open_page(urls.BASE_URL)
        user_page.auth(create_new_user)

        order_list.click_button_order_list()
        order_total_for_today = int(order_list.text_total_orders_for_today())
        build_page.click_constructor()
        order_list.drag_and_drop_ingredient_to_burger_side()
        build_page.click_make_order_button()
        order_list.wait_until_text_is_visible()
        order_list.wait_order_number_change()
        order_list.close_order_popup()
        order_list.click_button_order_list()

        assert order_total_for_today + 1 == int(order_list.text_total_orders_for_today())
    
    allure.title('При заведении нового заказа счётчик "Выполнено за всё время" увеличивается')
    def test_order_list_total_counter_increase(self, driver, create_new_user):
        order_list = OrderListPage(driver)
        user_page = UserAccountPage(driver)
        build_page = BuildBurgerPage(driver)

        user_page.open_page(urls.BASE_URL)
        user_page.auth(create_new_user)

        order_list.click_button_order_list()
        order_for_all_time = int(order_list.text_order_all_time())
        build_page.click_constructor()
        order_list.drag_and_drop_ingredient_to_burger_side()
        build_page.click_make_order_button()
        order_list.wait_until_text_is_visible()
        order_list.wait_order_number_change()
        order_list.close_order_popup()
        order_list.click_button_order_list()

        assert order_for_all_time + 1 == int(order_list.text_order_all_time())


    @allure.title('Заказ перемещён в блок "В работе"')
    def test_order_in_process_list(self, driver, create_new_user):
        page = BuildBurgerPage(driver)
        user_page = UserAccountPage(driver)
        page.open_page(urls.BASE_URL)
        user_page.auth(create_new_user)
        page.wait_for_clickability(BurgerLocators.INGREDIENT)
        page.make_order(BurgerLocators.INGREDIENT)
        page.wait_order_number_change()
        order_number = page.get_text_from_element(*BurgerLocators.ORDER_NUMBER)
        page.wait_for_visibility(BurgerLocators.CONFIRMATION_POPUP)
        page.minimize_order_popup()
        page.click_feed_button()
        page.wait_for_visibility(ol_loc.DONE_ALL_TIME)
        order_list_page = OrderListPage(page.driver)
        order_in_progress = order_list_page.order_number_in_progress()
        assert order_number in order_in_progress
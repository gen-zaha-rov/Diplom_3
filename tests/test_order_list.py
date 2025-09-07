import allure
import pytest

import urls
from locators import order_list_locators as ol_loc, build_burger_locators as bb_loc
from pages.order_list_page import OrderListPage
from pages.build_burger_page import BuildBurgerPage



@pytest.mark.usefixtures('driver', 'auth')
class TestOrderList:

    @allure.title('Детали заказа')
    def test_order_details(self):
        order_list = OrderListPage(self.driver)
        order_list.open_page(urls.ORDER_LIST)
        order_list.wait_for_clickability(ol_loc.ORDER_FROM_LIST, 7)
        order_list.click_order()
        assert order_list.driver.find_element(*ol_loc.ORDER_POPUP)

    @allure.title('Заказ пользователя в Ленте заказов')
    def test_user_order_in_list(self):
        page = BuildBurgerPage(self.driver)
        page.open_page(urls.BASE_URL)
        page.wait_for_clickability(bb_loc.INGREDIENT, 7)
        page.make_order(bb_loc.INGREDIENT)
        page.wait_for_visibility(bb_loc.CONFIRMATION_POPUP, 7)
        page.wait_order_number()
        order_number = '#0' + page.get_text(bb_loc.ORDER_NUMBER)
        page.minimize_order_popup()
        page.click_feed_button()
        page.wait_for_visibility(ol_loc.DONE_ALL_TIME, 7)
        assert page.driver.find_element(*(ol_loc.order_number_in_list(order_number)))

    @allure.title('Cчётчик {counter_type}')
    @pytest.mark.parametrize("counter_type, locator", [("Выполнено за всё время", ol_loc.DONE_ALL_TIME),
                                                       ("Выполнено за сегодня", ol_loc.DONE_TODAY)],
                             ids=["during all time", "during today"])
    def test_counter_done_all(self, counter_type, locator):
        page = BuildBurgerPage(self.driver)
        page.open_page(urls.ORDER_LIST)
        page.wait_for_clickability(locator, 7)
        count_before_new_order = page.get_text(locator)
        page.click_constructor()
        page.wait_for_clickability(bb_loc.INGREDIENT, 7)
        page.make_order(bb_loc.INGREDIENT)
        page.wait_order_number()
        order_number = '#0' + page.get_text(bb_loc.ORDER_NUMBER)
        page.wait_for_visibility(bb_loc.CONFIRMATION_POPUP, 7)
        page.minimize_order_popup()
        page.click_feed_button()
        page.wait_for_visibility(locator, 7)
        
        # Wait for the new order to appear in the feed
        page.wait_for_visibility(ol_loc.order_number_in_list(order_number), 7)
        
        count_after_new_order = page.get_text(locator)
        count_before = int(count_before_new_order)
        count_after = int(count_after_new_order)
        
        # The counter should increase after a new order is placed and processed
        assert count_after > count_before

    @allure.title('Заказ перемещён в блок "В работе"')
    def test_order_in_process_list(self):
        page = BuildBurgerPage(self.driver)
        page.open_page(urls.BASE_URL)
        page.wait_for_clickability(bb_loc.INGREDIENT, 7)
        page.make_order(bb_loc.INGREDIENT)
        page.wait_order_number()
        order_number = page.get_text(bb_loc.ORDER_NUMBER)
        page.wait_for_visibility(bb_loc.CONFIRMATION_POPUP, 7)
        page.minimize_order_popup()
        page.click_feed_button()
        page.wait_for_visibility(ol_loc.DONE_ALL_TIME, 7)
        assert page.get_text(ol_loc.LAST_FROM_IN_PROCESS)[1:] == order_number
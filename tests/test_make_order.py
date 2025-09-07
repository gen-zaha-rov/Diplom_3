import allure
import pytest
from selenium.webdriver.support.wait import WebDriverWait

import urls
from locators import order_list_locators as ol_loc, build_burger_locators as bb_loc
from pages.build_burger_page import BuildBurgerPage



@pytest.mark.usefixtures('driver', 'auth')
class TestBuildBurgerPage:

    @allure.title("Переход к Конструктору")
    def test_open_build_burger(self):
        order_page = BuildBurgerPage(self.driver)
        order_page.open_page(urls.ORDER_LIST)
        order_page.click_constructor()
        order_page.wait_for_visibility(bb_loc.ORDER_SECTION, 7)
        assert order_page.driver.current_url == f'{urls.BASE_URL}/'

    @allure.title("Переход к Ленте заказов")
    def test_open_list(self):
        order_page = BuildBurgerPage(self.driver)
        order_page.open_page(urls.BASE_URL)
        order_page.click_feed_button()
        order_page.wait_for_visibility(ol_loc.DONE_ALL_TIME, 7)
        assert order_page.driver.current_url == urls.ORDER_LIST

    @allure.title("Переход к окну ингредиента")
    def test_open_ingredient_window(self):
        order_page = BuildBurgerPage(self.driver)
        order_page.open_page(urls.BASE_URL)
        order_page.wait_for_clickability(bb_loc.INGREDIENT, 7)
        order_page.click_ingredient()
        order_page.wait_for_visibility(bb_loc.HEADER_INGREDIENT_POPUP, 7)
        assert order_page.get_text(bb_loc.INGREDIENT_NAME) == order_page.get_text(bb_loc.INGREDIENT_NAME_IN_POPUP)

    @allure.title("Скрытие окна ингредиента")
    def test_minimize_ingredient_window(self):
        order_page = BuildBurgerPage(self.driver)
        order_page.open_page(urls.BASE_URL)
        order_page.wait_for_clickability(bb_loc.INGREDIENT, 7)
        order_page.click_ingredient()
        order_page.wait_for_visibility(bb_loc.HEADER_INGREDIENT_POPUP, 7)
        order_page.minimize_ingredient_popup()
        assert 'Modal_modal_opened__3ISw4' not in order_page.get_value(bb_loc.POP_UP_SECTION, "class")

    @allure.title("Cчетчик ингредиента")
    def test_ingredient_counter(self):
        order_page = BuildBurgerPage(self.driver)
        order_page.open_page(urls.BASE_URL)
        order_page.wait_for_clickability(bb_loc.INGREDIENT, 7)
        before_adding = int(order_page.get_text(bb_loc.INGREDIENT_COUNTER))
        order_page.add_ingredient_to_order(bb_loc.INGREDIENT)
        WebDriverWait(order_page.driver, 7).until(
            lambda d: int(order_page.get_text(bb_loc.INGREDIENT_COUNTER)) > before_adding
        )
        after_adding = int(order_page.get_text(bb_loc.INGREDIENT_COUNTER))
        assert before_adding < after_adding

    @allure.title("Создание заказа авторизованным пользователем")
    def test_make_order_by_authorized_user(self, auth):
        order_page = BuildBurgerPage(self.driver)
        order_page.open_page(urls.BASE_URL)
        order_page.wait_for_clickability(bb_loc.INGREDIENT, 7)
        order_page.make_order(bb_loc.INGREDIENT)
        order_page.wait_for_visibility(bb_loc.CONFIRMATION_POPUP, 7)
        assert order_page.driver.find_element(*bb_loc.CONFIRMATION_POPUP)
import allure
import urls
from pages.build_burger_page import BuildBurgerPage


class TestBuildBurgerPage:

    @allure.title("Переход к Конструктору")
    def test_open_build_burger(self, driver):
        order_page = BuildBurgerPage(driver)
        order_page.open_page(urls.BASE_URL)
        order_page.click_constructor()
        assert order_page.get_url() == f'{urls.BASE_URL}/'

    @allure.title("Переход к Ленте заказов")
    def test_open_list(self, driver):
        order_page = BuildBurgerPage(driver)
        order_page.open_page(urls.BASE_URL)
        order_page.click_feed_button()
        assert order_page.get_url() == urls.ORDER_LIST

    @allure.title("Переход к окну ингредиента")
    def test_open_ingredient_window(self, driver):
        order_page = BuildBurgerPage(driver)
        order_page.open_page(urls.BASE_URL)
        order_page.wait_for_ingredient_clickability()
        order_page.click_ingredient()
        assert order_page.display_ingredient_info()

    @allure.title("Скрытие окна ингредиента")
    def test_minimize_ingredient_window(self, driver):
        order_page = BuildBurgerPage(driver)
        order_page.open_page(urls.BASE_URL)
        order_page.wait_for_ingredient_clickability()
        order_page.click_ingredient()
        order_page.minimize_ingredient_popup()
        assert order_page.check_if_closed()

    @allure.title("Cчетчик ингредиента")
    def test_ingredient_counter(self, driver):
        order_page = BuildBurgerPage(driver)
        order_page.open_page(urls.BASE_URL)
        order_page.wait_for_ingredient_clickability()
        before_adding = order_page.get_ingredient_counter_value()
        order_page.add_first_ingredient_to_order()
        order_page.wait_ingredient_counter()
        after_adding = order_page.get_ingredient_counter_value()
        assert before_adding < after_adding

    @allure.title("Создание заказа авторизованным пользователем")
    def test_make_order_by_authorized_user(self, driver, create_new_user):
        order_page = BuildBurgerPage(driver)
        order_page.open_page(urls.BASE_URL)
        order_page.auth(create_new_user)
        order_page.wait_for_ingredient_clickability()
        order_page.make_order_with_first_ingredient()
        order_page.wait_for_confirmation_popup()
        assert order_page.check_confirmation_popup_displayed()
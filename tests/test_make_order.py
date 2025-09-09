import allure
import urls
from locators import order_list_locators as ol_loc
from locators.build_burger_locators import BurgerLocators
from pages.build_burger_page import BuildBurgerPage
from pages.user_account_page import UserAccountPage


class TestBuildBurgerPage:

    @allure.title("Переход к Конструктору")
    def test_open_build_burger(self, driver):
        order_page = BuildBurgerPage(driver)
        order_page.open_page(urls.ORDER_LIST)
        order_page.click_constructor()
        order_page.wait_for_visibility(BurgerLocators.ORDER_SECTION)
        assert order_page.get_url() == f'{urls.BASE_URL}/'

    @allure.title("Переход к Ленте заказов")
    def test_open_list(self, driver):
        order_page = BuildBurgerPage(driver)
        order_page.open_page(urls.BASE_URL)
        order_page.click_feed_button()
        order_page.wait_for_visibility(ol_loc.DONE_ALL_TIME)
        assert order_page.get_url() == urls.ORDER_LIST

    @allure.title("Переход к окну ингредиента")
    def test_open_ingredient_window(self, driver):
        order_page = BuildBurgerPage(driver)
        order_page.open_page(urls.BASE_URL)
        order_page.wait_for_clickability(BurgerLocators.INGREDIENT)
        order_page.click_ingredient()
        order_page.wait_for_visibility(BurgerLocators.HEADER_INGREDIENT_POPUP)
        assert order_page.get_text_from_element(*BurgerLocators.INGREDIENT_NAME) == order_page.get_text_from_element(*BurgerLocators.INGREDIENT_NAME_IN_POPUP)

    @allure.title("Скрытие окна ингредиента")
    def test_minimize_ingredient_window(self, driver):
        order_page = BuildBurgerPage(driver)
        order_page.open_page(urls.BASE_URL)
        order_page.wait_for_clickability(BurgerLocators.INGREDIENT)
        order_page.click_ingredient()
        order_page.wait_for_visibility(BurgerLocators.HEADER_INGREDIENT_POPUP)
        order_page.minimize_ingredient_popup()
        assert 'Modal_modal_opened__3ISw4' not in order_page.get_value(*BurgerLocators.POP_UP_SECTION, value="class")

    @allure.title("Cчетчик ингредиента")
    def test_ingredient_counter(self, driver):
        order_page = BuildBurgerPage(driver)
        order_page.open_page(urls.BASE_URL)
        order_page.wait_for_clickability(BurgerLocators.INGREDIENT)
        before_adding = int(order_page.get_text_from_element(*BurgerLocators.INGREDIENT_COUNTER))
        order_page.add_ingredient_to_order(BurgerLocators.INGREDIENT)
        order_page.wait_ingredient_counter()
        after_adding = int(order_page.get_text_from_element(*BurgerLocators.INGREDIENT_COUNTER))
        assert before_adding < after_adding

    @allure.title("Создание заказа авторизованным пользователем")
    def test_make_order_by_authorized_user(self, driver, create_new_user):
        order_page = BuildBurgerPage(driver)
        user_page = UserAccountPage(driver)
        order_page.open_page(urls.BASE_URL)
        user_page.auth(create_new_user)
        order_page.wait_for_clickability(BurgerLocators.INGREDIENT)
        order_page.make_order(BurgerLocators.INGREDIENT)
        order_page.wait_for_visibility(BurgerLocators.CONFIRMATION_POPUP)
        assert order_page.find_element(*BurgerLocators.CONFIRMATION_POPUP)
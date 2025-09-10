import allure
import urls
from pages.user_account_page import UserAccountPage


class TestUserAccountPage:

    @allure.title("Вход в Личный Кабинет")
    def test_user_account(self, driver, create_new_user):
        profile = UserAccountPage(driver)
        profile.auth(create_new_user)
        profile.click_user_account()
        profile.wait_for_logout_button()
        assert profile.get_url() == urls.USER_PROFILE

    @allure.title("Переход в Историю заказов")
    def test_order_history(self, driver, create_new_user):
        profile = UserAccountPage(driver)
        profile.auth(create_new_user)
        profile.click_user_account()
        profile.click_order_history()
        assert profile.get_url() == urls.ORDER_HISTORY

    @allure.title("Выход из Личного Кабинета")
    def test_logout(self, driver, create_new_user):
        profile = UserAccountPage(driver)
        profile.auth(create_new_user)
        profile.click_user_account()
        profile.click_logout()
        assert profile.get_url() == urls.LOGIN_USER
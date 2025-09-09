import allure

import urls
from locators import user_related_locators as loc
from pages.user_account_page import UserAccountPage


class TestUserAccountPage:

    @allure.title("Вход в Личный Кабинет")
    def test_user_account(self, driver, create_new_user):
        profile = UserAccountPage(driver)
        profile.open_page(urls.BASE_URL)
        profile.auth(create_new_user)
        profile.click_user_account()
        profile.wait_for_visibility(loc.LOGOUT_BUTTON)
        assert profile.get_url() == urls.USER_PROFILE

    @allure.title("Переход в Историю заказов")
    def test_order_history(self, driver, create_new_user):
        profile = UserAccountPage(driver)
        profile.open_page(urls.BASE_URL)
        profile.auth(create_new_user)
        profile.click_user_account()
        profile.wait_for_visibility(loc.LOGOUT_BUTTON)
        profile.click_order_history()
        assert profile.get_url() == urls.ORDER_HISTORY

    @allure.title("Выход из Личного Кабинета")
    def test_logout(self, driver, create_new_user):
        profile = UserAccountPage(driver)
        profile.open_page(urls.BASE_URL)
        profile.auth(create_new_user)
        profile.click_user_account()
        profile.wait_for_visibility(loc.LOGOUT_BUTTON)
        profile.click_logout()
        profile.wait_for_visibility(loc.LOGIN_BUTTON)
        assert profile.get_url() == urls.LOGIN_USER
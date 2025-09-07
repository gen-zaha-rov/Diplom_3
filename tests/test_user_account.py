import allure
import pytest

import urls
from locators import user_related_locators as loc
from pages.user_account_page import UserAccountPage



@pytest.mark.usefixtures('driver', 'auth')
class TestUserAccountPage:

    @allure.title("Вход в Личный Кабинет")
    def test_user_account(self):
        profile = UserAccountPage(self.driver)
        profile.open_page(urls.BASE_URL)
        profile.click_user_account()
        profile.wait_for_visibility(loc.LOGOUT_BUTTON, 7)
        assert profile.driver.current_url == urls.USER_PROFILE

    @allure.title("Переход в Историю заказов")
    def test_order_history(self):
        profile = UserAccountPage(self.driver)
        profile.open_page(urls.BASE_URL)
        profile.click_user_account()
        profile.wait_for_visibility(loc.LOGOUT_BUTTON, 7)
        profile.click_order_history()
        assert profile.driver.current_url == urls.ORDER_HISTORY

    @allure.title("Выход из Личного Кабинета")
    def test_logout(self):
        profile = UserAccountPage(self.driver)
        profile.open_page(urls.BASE_URL)
        profile.click_user_account()
        profile.wait_for_visibility(loc.LOGOUT_BUTTON, 7)
        profile.click_logout()
        profile.wait_for_visibility(loc.LOGIN_BUTTON, 7)
        assert profile.driver.current_url == urls.LOGIN_USER
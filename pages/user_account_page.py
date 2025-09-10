import allure
import urls

from locators import user_related_locators as loc
from pages.base_page import BasePage


class UserAccountPage(BasePage):

    @allure.step('Вход в аккаунт')
    def auth(self, create_user):
        email, password = create_user

        self.open_page(urls.LOGIN_USER)
        self.enter_text(*loc.EMAIL_FIELD_FOR_AUTH, text=email)
        self.enter_text(*loc.PASSWORD_AUTH_FIELD, text=password)
        self.click_element(*loc.LOGIN_BUTTON)

    @allure.step('Ожидание кнопки «Профиль»')
    def wait_for_logout_button(self):
        self.wait_for_clickability(loc.LOGOUT_BUTTON)    

    @allure.step('Нажатие на кнопку "Личный кабинет"')
    def click_user_account(self):
        self.wait_for_clickability(loc.USER_ACCOUNT_BUTTON)
        self.click_element(*loc.USER_ACCOUNT_BUTTON)

    @allure.step('Переход на вкладку "История заказов"')
    def click_order_history(self):
        self.wait_for_clickability(loc.ORDER_HISTORY)
        self.click_element(*loc.ORDER_HISTORY)

    @allure.step('Нажатие на кнопку "Выход"')
    def click_logout(self):
        self.wait_for_clickability(loc.LOGOUT_BUTTON)
        self.click_element(*loc.LOGOUT_BUTTON)
        self.wait_for_visibility(loc.ENTER_TEXT)
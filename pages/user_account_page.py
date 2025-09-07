import allure
from locators import user_related_locators as loc
from pages.base_page import BasePage


class UserAccountPage(BasePage):

    @allure.step('Нажатие на кнопку "Личный кабинет"')
    def click_user_account(self):
        self.driver.find_element(*loc.USER_ACCOUNT_BUTTON).click()

    @allure.step('Переход на вкладку "История заказов"')
    def click_order_history(self):
        self.driver.find_element(*loc.ORDER_HISTORY).click()

    @allure.step('Нажатие на кнопку "Выход"')
    def click_logout(self):
        self.driver.find_element(*loc.LOGOUT_BUTTON).click()
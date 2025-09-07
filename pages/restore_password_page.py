import allure
from locators import user_related_locators as loc
from pages.base_page import BasePage


class RestorePasswordPage(BasePage):

    @allure.step('Нажать на кнопку "Восстановить пароль"')
    def click_restore_password_link(self):
        self.scroll_to_element(loc.RESTORE_PASSWORD_LINK)
        self.driver.find_element(*loc.RESTORE_PASSWORD_LINK).click()

    @allure.step('Ввести email в поле "Email"')
    def fill_email(self, email):
        self.driver.find_element(*loc.EMAIL_FIELD).send_keys(email)

    @allure.step('Нажать на кнопку "Восстановить"')
    def click_restore_btn(self):
        self.driver.find_element(*loc.RESTORE_PASSWORD_BUTTON).click()

    @allure.step('Нажать на кнопку показать/скрыть пароль (глаз)')
    def click_eye_btn(self):
        self.driver.find_element(*loc.PASSWORD_EYE_BUTTON).click()

    def check_email(self, email):
        self.fill_email(email)
        self.click_restore_btn()
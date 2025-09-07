import allure
import pytest
from selenium.webdriver.common.by import By

import urls
from locators import user_related_locators as loc
from pages.restore_password_page import RestorePasswordPage


@allure.suite("Восстановление пароля")
@pytest.mark.usefixtures('driver')
class TestRestorePassword:

    @allure.title("Зайти на страницу восстановления пароля")
    def test_click_restore_password_link(self):
        restore_pass = RestorePasswordPage(self.driver)
        restore_pass.open_page(urls.LOGIN_USER)
        restore_pass.wait_for_visibility(loc.RESTORE_PASSWORD_LINK, 7)
        restore_pass.click_restore_password_link()
        restore_pass.wait_for_visibility(loc.RESTORE_PASSWORD_BUTTON, 7)
        assert restore_pass.driver.current_url == urls.FORGOT_PASSWORD

    @allure.title("Ввести email для восстановления пароля")
    def test_fill_email(self, create_new_user):
        reset_page = RestorePasswordPage(self.driver)
        reset_page.open_page(urls.FORGOT_PASSWORD)
        reset_page.fill_email(create_new_user[0])
        assert reset_page.get_value(loc.EMAIL_FIELD, 'value') == create_new_user[0]

    @allure.title("Кнопка 'Восстановить'")
    def test_restore_btn(self, create_new_user):
        restore_pass = RestorePasswordPage(self.driver)
        restore_pass.open_page(urls.FORGOT_PASSWORD)
        restore_pass.fill_email(create_new_user[0])
        restore_pass.click_restore_btn()
        restore_pass.wait_for_visibility(loc.PASSWORD_EYE_BUTTON, 7)
        assert restore_pass.driver.current_url == urls.RESTORE_PASSWORD

    @allure.title("Кнопка показать/скрыть в поле ввода пароля")
    def test_eye_button(self, create_new_user):
        restore_pass = RestorePasswordPage(self.driver)
        restore_pass.open_page(urls.FORGOT_PASSWORD)
        restore_pass.fill_email(create_new_user[0])
        restore_pass.click_restore_btn()
        restore_pass.wait_for_visibility(loc.PASSWORD_EYE_BUTTON, 7)
        restore_pass.click_eye_btn()
        # Проверка того, что поле ввода пароля изменило тип с password на text (кнопка глаза работает)
        password_input = restore_pass.driver.find_element(By.XPATH, '//input[@type="password" or @type="text"]')
        assert password_input.get_attribute('type') == 'text'
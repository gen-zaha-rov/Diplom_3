import allure

import urls
from locators import user_related_locators as loc
from pages.restore_password_page import RestorePasswordPage


@allure.suite("Восстановление пароля")
class TestRestorePassword:

    @allure.step("Зайти на страницу восстановления пароля")
    def test_click_restore_password_link(self, driver):
        restore_pass = RestorePasswordPage(driver)
        restore_pass.open_page(urls.LOGIN_USER)
        restore_pass.wait_for_visibility(loc.RESTORE_PASSWORD_LINK)
        restore_pass.click_restore_password_link()
        restore_pass.wait_for_visibility(loc.RESTORE_PASSWORD_BUTTON)
        assert restore_pass.get_url() == urls.FORGOT_PASSWORD

    @allure.step("Ввести email для восстановления пароля")
    def test_fill_email(self, driver, create_new_user):
        reset_page = RestorePasswordPage(driver)
        reset_page.open_page(urls.FORGOT_PASSWORD)
        reset_page.fill_email(create_new_user[0])
        assert reset_page.get_value(*loc.EMAIL_FIELD, value='value') == create_new_user[0]

    @allure.step("Кнопка 'Восстановить'")
    def test_restore_btn(self, driver, create_new_user):
        restore_pass = RestorePasswordPage(driver)
        restore_pass.open_page(urls.FORGOT_PASSWORD)
        restore_pass.fill_email(create_new_user[0])
        restore_pass.click_restore_btn()
        restore_pass.wait_for_visibility(loc.PASSWORD_EYE_BUTTON)
        assert restore_pass.get_url() == urls.RESTORE_PASSWORD

    @allure.step("Кнопка показать/скрыть в поле ввода пароля")
    def test_eye_button(self, driver, create_new_user):
        restore_pass = RestorePasswordPage(driver)
        restore_pass.open_page(urls.FORGOT_PASSWORD)
        restore_pass.fill_email(create_new_user[0])
        restore_pass.click_restore_btn()
        restore_pass.wait_for_visibility(loc.PASSWORD_EYE_BUTTON)
        restore_pass.click_eye_btn()
        # Проверка того, что поле ввода пароля изменило тип с password на text (кнопка глаза работает)
        password_input = restore_pass.find_element(*loc.PASSWORD_FIELD_DISPLAYED_DATA)
        assert password_input.get_attribute('type') == 'text'
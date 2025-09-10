import allure
import urls
from pages.restore_password_page import RestorePasswordPage


@allure.suite("Восстановление пароля")
class TestRestorePassword:

    @allure.step("Зайти на страницу восстановления пароля")
    def test_click_restore_password_link(self, driver):
        restore_pass = RestorePasswordPage(driver)
        restore_pass.click_user_account()
        restore_pass.click_restore_password_link()
        assert restore_pass.get_url() == urls.FORGOT_PASSWORD

    @allure.step("Ввести email для восстановления пароля")
    def test_fill_email(self, driver, create_new_user):
        reset_page = RestorePasswordPage(driver)
        reset_page.click_user_account()
        reset_page.click_restore_password_link()
        reset_page.fill_email(create_new_user[0])
        reset_page.click_restore_btn()
        reset_page.wait_save_button_to_display()
        assert reset_page.get_url() == urls.RESTORE_PASSWORD

    @allure.step("Кнопка 'Восстановить'")
    def test_restore_btn(self, driver, create_new_user):
        restore_pass = RestorePasswordPage(driver)
        restore_pass.click_user_account()
        restore_pass.click_restore_password_link()
        restore_pass.fill_email(create_new_user[0])
        restore_pass.click_restore_btn()
        restore_pass.wait_eye_button_to_display()
        assert restore_pass.get_url() == urls.RESTORE_PASSWORD

    @allure.step("Кнопка показать/скрыть в поле ввода пароля")
    def test_eye_button(self, driver, create_new_user):
        restore_pass = RestorePasswordPage(driver)
        restore_pass.click_user_account()
        restore_pass.click_restore_password_link()
        restore_pass.fill_email(create_new_user[0])
        restore_pass.click_restore_btn()
        restore_pass.click_eye_btn()
        # Проверка того, что поле ввода пароля изменило тип с password на text (кнопка глаза работает)
        password_input = restore_pass.check_data_type_in_pass_field()
        assert password_input.get_attribute('type') == 'text'
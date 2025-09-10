import allure
from locators import user_related_locators as loc
from pages.base_page import BasePage


class RestorePasswordPage(BasePage):

    @allure.step('Нажатие на кнопку "Личный кабинет"')
    def click_user_account(self):
        self.wait_for_clickability(loc.USER_ACCOUNT_BUTTON)
        self.click_element(*loc.USER_ACCOUNT_BUTTON)
    
    @allure.step('Нажать на кнопку "Восстановить пароль"')
    def click_restore_password_link(self):
        self.wait_for_visibility(loc.RESTORE_PASSWORD_LINK)
        self.scroll_to_element(*loc.RESTORE_PASSWORD_LINK)
        self.click_element(*loc.RESTORE_PASSWORD_LINK)

    @allure.step('Ввести email в поле "Email"')
    def fill_email(self, email):
        self.wait_for_visibility(loc.EMAIL_FIELD)
        self.enter_text(*loc.EMAIL_FIELD, text=email)

    @allure.step('Проверить присутствие кнопки "Сохранить"')
    def wait_save_button_to_display(self):
        return self.wait_for_visibility(loc.SAVE_BUTTON)
    
    @allure.step('Проверить присутствие кнопки глаз в поле пароля')
    def wait_eye_button_to_display(self):
        return self.wait_for_visibility(loc.PASSWORD_EYE_BUTTON)
    
    @allure.step('Проверить тип данных в поле пароля')
    def check_data_type_in_pass_field(self):
        return self.find_element(*loc.PASSWORD_FIELD_DISPLAYED_DATA)    

    @allure.step('Нажать на кнопку "Восстановить"')
    def click_restore_btn(self):
        self.click_element(*loc.RESTORE_PASSWORD_BUTTON)

    @allure.step('Нажать на кнопку показать/скрыть пароль (глаз)')
    def click_eye_btn(self):
        self.click_element(*loc.PASSWORD_EYE_BUTTON)

    def check_email(self, email):
        self.fill_email(email)
        self.click_restore_btn()
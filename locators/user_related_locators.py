from selenium.webdriver.common.by import By


# Авторизация
EMAIL_FIELD_FOR_AUTH = (By.XPATH, '//input[@name="name" or @type="email"]')
PASSWORD_AUTH_FIELD = (By.XPATH, '//input[@name="Пароль" or @type="password"]')
LOGIN_BUTTON = (By.XPATH, './/button[contains(text(), "Войти")]')
HEADER_MAIN_PAGE = (By.XPATH, './/h1[text()="Соберите бургер"]')

# Восстановление пароля
RESTORE_PASSWORD_LINK = (By.XPATH, './/*[@href="/forgot-password"]')
EMAIL_FIELD = (By.XPATH, './/*[@class="text input__textfield text_type_main-default"]')
RESTORE_PASSWORD_BUTTON = (By.XPATH, '//*[@id="root"]/div/main/div/form/button')
PASSWORD_FIELD = (By.XPATH,'//div[@class="input pr-6 pl-6 input_type_password input_size_default"]')
PASSWORD_EYE_BUTTON = (By.XPATH,'.//*[@class="input__icon input__icon-action"]')
PASSWORD_FIELD_DISPLAYED_DATA = (By.XPATH, '//input[@type="password" or @type="text"]')
SAVE_BUTTON = (By.XPATH, '//button[text()="Сохранить"]')

# Личный кабинет
ENTER_TEXT = (By.XPATH, '//h2[text()="Вход"]')
USER_ACCOUNT_BUTTON = (By.XPATH, './/*[@href="/account"]')
ORDER_HISTORY = (By.XPATH, './/*[@href="/account/order-history"]')
LOGOUT_BUTTON = (By.XPATH, '//button[contains(@class, "Account_button__14Yp3") and contains(text(), "Выход")]')
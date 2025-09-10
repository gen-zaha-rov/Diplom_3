from selenium.webdriver.common.by import By

# Локаторы со страницы "Соберите бургер"
class BurgerLocators:
    BUILD_BURGER = (By.XPATH, '//h1[text() = "Соберите бургер"]') 
    CONSTRUCTOR_BUTTON = (By.XPATH, './/p[contains(text(),"Конструктор")]')
    ORDER_LIST_BUTTON = (By.XPATH, './/*[@href="/feed"]')
    INGREDIENT = (By.XPATH, './/ul[@class="BurgerIngredients_ingredients__list__2A-mT"][1]/a[1]')
    INGREDIENT_NAME = (By.XPATH, './/ul[@class="BurgerIngredients_ingredients__list__2A-mT"][1]/a[1]/child::p')
    HEADER_INGREDIENT_POPUP = (By.XPATH, './/h2[text()="Детали ингредиента"]')
    INGREDIENT_NAME_IN_POPUP = (By.XPATH, './/h2[text()="Детали ингредиента"]/following-sibling::p')
    BUN_INFO = (By.XPATH, '//h2[text() = "Детали ингредиента"]')
    POP_UP_SECTION = (By.XPATH, './/section[contains(@class, "Modal_modal__P3_V5")]')
    CLOSE_DETAILS_POPUP = (By.XPATH, './/div[@class="Modal_modal__contentBox__sCy8X pt-10 pb-15"]'
                                 '/following-sibling::button')
    INGREDIENT_COUNTER = (By.XPATH, './/ul[@class="BurgerIngredients_ingredients__list__2A-mT"][1]/a[1]'
                                '/div[@class="counter_counter__ZNLkj counter_default__28sqi"]/p')
    ORDER_SECTION = (By.XPATH, './/li[@class="BurgerConstructor_basket__listItem__aWMu1 mr-4"][2]/div')
    MAKE_ORDER_BUTTON = (By.XPATH, './/*[@class="button_button__33qZ0 button_button_type_primary__1O7Bx '
                               'button_button_size_large__G21Vg"]')
    CONFIRMATION_POPUP = (By.XPATH, './/*[@class="Modal_modal__contentBox__sCy8X pt-30 pb-30"]')
    CLOSE_ORDER_POPUP = (By.XPATH, './/div[@class="Modal_modal__contentBox__sCy8X pt-30 pb-30"]'
                               '/following-sibling::button')
    ORDER_NUMBER = (By.XPATH, './/*[@class="Modal_modal__title_shadow__3ikwq Modal_modal__title__2L34m '
                          'text text_type_digits-large mb-8"]')
    EMAIL_FIELD_FOR_AUTH = (By.XPATH, '//input[@name="name" or @type="email"]')
    PASSWORD_AUTH_FIELD = (By.XPATH, '//input[@name="Пароль" or @type="password"]')
    LOGIN_BUTTON = (By.XPATH, './/button[contains(text(), "Войти")]')
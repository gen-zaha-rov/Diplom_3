from selenium.webdriver.common.by import By


ORDER_FROM_LIST = (By.XPATH, './/li[@class="OrderHistory_listItem__2x95r mb-6"][1]')
ORDER_POPUP = (By.XPATH, './/*[@class="Modal_orderBox__1xWdi Modal_modal__contentBox__sCy8X p-10"]')
MODAL_ORDER_IN_PROCESSING = (By.XPATH, ".//p[text()='Ваш заказ начали готовить']")
CLOSE_ORDER_POPUP = (By.XPATH, '(//button[@type="button" and contains(@class, "Modal_modal__close_modified")])[1]')
DONE_TODAY = (By.XPATH, './/p[contains(text(), "за сегодня")]/following-sibling::p')
DONE_ALL_TIME = (By.XPATH, './/p[contains(text(), "за все время")]/following-sibling::p')
LAST_FROM_IN_PROCESS = (By.XPATH, './/ul[@class="OrderFeed_orderList__cBvyi"]/li[1]')
ORDER_NUMBER_IN_PROGRESS = (By.XPATH, "//li[contains(@class, 'text') and contains(@class, 'text_type_digits-default') and contains(@class, 'mb-2')]") 
BUN = (By.XPATH, '//p[text() = "Флюоресцентная булка R2-D3"]')
BURGER_SIDE = (By.XPATH, '//section[contains(@class, "BurgerConstructor_basket")]') 
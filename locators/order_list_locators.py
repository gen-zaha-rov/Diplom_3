from selenium.webdriver.common.by import By


ORDER_FROM_LIST = (By.XPATH, './/li[@class="OrderHistory_listItem__2x95r mb-6"][1]')
ORDER_POPUP = (By.XPATH, './/*[@class="Modal_orderBox__1xWdi Modal_modal__contentBox__sCy8X p-10"]')
CLOSE_ORDER_POPUP = (By.CSS_SELECTOR, 'button.Modal_modal__close_modified__3V5XS.Modal_modal__close__TnseK')
DONE_TODAY = (By.XPATH, './/p[contains(text(), "за сегодня")]/following-sibling::p')
DONE_ALL_TIME = (By.XPATH, './/p[contains(text(), "за все время")]/following-sibling::p')
LAST_FROM_IN_PROCESS = (By.XPATH, './/ul[@class="OrderFeed_orderList__cBvyi"]/li[1]')


def order_number_in_list(order_number):
    return By.XPATH, (f'.//*[@class="OrderHistory_textBox__3lgbs mb-6"]/p[@class="text text_type_digits-default" '
                      f'and contains(text(), "{order_number}")]')


def in_process_order_number(order_number: str):
    #  Возвращает путь для номера заказа в списке "В работе".
    #  Соответствует любому элементу списка, содержащему предоставленный номер (с или без префикса '#').
    return By.XPATH, (f'.//ul[@class="OrderFeed_orderList__cBvyi"]/li//p[contains(text(), "{order_number}")]')


def anywhere_in_feed_order_number(order_number: str):
    #  Возвращает путь для номера заказа в ленте заказов.
    #  Соответствует любому элементу списка, содержащему предоставленный номер (с или без префикса '#').
    prefixed_number = f"#{order_number}"
    return By.XPATH, f'.//li//p[contains(text(), "{order_number}") or contains(text(), "{prefixed_number}")]'
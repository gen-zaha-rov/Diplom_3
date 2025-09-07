import allure
import pytest
import requests
from selenium import webdriver
from selenium.webdriver.chrome.options import Options

import urls
from pages.base_page import BasePage
import data as dt
from locators import user_related_locators as loc



def pytest_addoption(parser):
    parser.addoption('--driver_name', type=str, default='chrome', help='choose one of drivers: chrome or firefox')
    parser.addoption('--headless', action='store_true', default=False, help='run browser in headless mode')
    parser.addoption('--window_width', type=int, default=1300, help='browser window width')
    parser.addoption('--window_height', type=int, default=800, help='browser window height')


@pytest.fixture(scope="class", autouse=True)
def driver(request):
    driver_name = request.config.getoption('--driver_name')
    headless = request.config.getoption('--headless')
    width = request.config.getoption('--window_width')
    height = request.config.getoption('--window_height')
    with allure.step('Открыть браузер'):
        if driver_name == 'firefox':
            options = webdriver.FirefoxOptions()
            if headless:
                options.add_argument('-headless')
            options.add_argument(f'--width={width}')
            options.add_argument(f'--height={height}')
            request.cls.driver = webdriver.Firefox(options=options)
        else:
            options = Options()
            if headless:
                options.add_argument('--headless=new')
                options.add_argument(f'--window-size={width},{height}')
            else:
                options.add_argument("--start-maximized")
            request.cls.driver = webdriver.Chrome(options=options)
    yield
    with allure.step('Закрыть браузер'):
        request.cls.driver.quit()


@allure.title("Создать пользователя")
@pytest.fixture(scope="class")
def create_new_user():
    email = dt.generate_email()
    password = dt.generate_random_string()
    data = {
        "email": email,
        "password": password,
        "name": dt.generate_random_string(4)
    }
    response_json = requests.post(url=urls.REGISTER_USER, data=data).json()
    yield email, password
    requests.delete(url=urls.USER_AUTH, headers={"Authorization": response_json["accessToken"]})


@pytest.fixture(scope="class")
def auth(driver, request, create_new_user):
    request.cls.driver.get(urls.LOGIN_USER)
    page = BasePage(request.cls.driver)
    page.wait_for_clickability(loc.EMAIL_FIELD_FOR_AUTH, 7)
    page.driver.find_element(*loc.EMAIL_FIELD_FOR_AUTH).send_keys(create_new_user[0])
    page.wait_for_clickability(loc.PASSWORD_AUTH_FIELD, 7)
    page.driver.find_element(*loc.PASSWORD_AUTH_FIELD).send_keys(create_new_user[1])
    page.wait_for_clickability(loc.LOGIN_BUTTON, 7)
    page.driver.find_element(*loc.LOGIN_BUTTON).click()
    page.wait_for_visibility(loc.HEADER_MAIN_PAGE, 7)
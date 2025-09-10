import pytest
import requests
from selenium import webdriver
from selenium.webdriver.chrome.options import Options

import urls
import helpers as hp



@pytest.fixture(scope="class", params=['chrome'])
def driver(request):
    if request.param == 'chrome':
        options = webdriver.ChromeOptions()
        browser = webdriver.Chrome(options=options)
    elif request.param == 'firefox':
        options = webdriver.FirefoxOptions()
        browser = webdriver.Firefox(options=options)
    else:
        raise ValueError(f"Неподдерживаемый браузер: {request.param}")

    browser.get(urls.BASE_URL)

    yield browser
    browser.quit()


@pytest.fixture(scope="function")
def create_new_user():
    email = hp.generate_email()
    password = hp.generate_random_string()
    data = {
        "email": email,
        "password": password,
        "name": hp.generate_random_string(4)
    }
    response_json = requests.post(url=urls.REGISTER_USER, data=data).json()
    yield email, password
    requests.delete(url=urls.USER_AUTH, headers={"Authorization": response_json["accessToken"]})

    
 
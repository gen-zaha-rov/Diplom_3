# Diplom_3

Набор автотестов на Selenium + Pytest для сайта `Stellar Burgers`.

## Установка и запуск

1) Создать и активировать venv (Windows PowerShell):
```
python -m venv venv
venv\Scripts\Activate.ps1
```

2) Установить зависимости:
```
pip install -r requirements.txt
```

3) Запуск тестов:
```
pytest -s -v

для дебага удобнее запускать штучно:
python -m pytest tests/test_make_order.py::TestBuildBurgerPage::test_open_build_burger -v
```

## Полезные опции

- Выбор браузера:
```
pytest --driver_name=chrome   # по умолчанию
pytest --driver_name=firefox
```

- Запуск без UI (headless) и размер окна:
```
pytest --headless --window_width=1300 --window_height=800
```

Можно комбинировать с выбором браузера.

## Структура

- `pages/` — PageObject-страницы
- `locators/` — локаторы
- `tests/` — тесты PyTest
- `conftest.py` — фикстуры, опции запуска
- `urls.py` — адреса
- `data.py` — генераторы данных

## Отчёты Allure

Установить CLI и собрать отчёт:
```
pytest --alluredir=allure-results
allure serve allure-results
```

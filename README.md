### Запуск автотестов для разных языков интерфейса
Решение, которое позволяет запускать автотесты для разных языков пользователей, передавая нужный язык в командной строке.

## Как запустить тесты:
- Клонировать репозиторий:
```
https://github.com/rerolll/automated_testing_different-languages_of_the_interface.git
```
- Перейти в папку тестов
```
cd/automated_testing_different-languages_of_the_interface
```
- Установить виртуальное окружение
```
python -m venv venv
```
- Активировать виртуальное окружение
```
source venv/Scripts/activate
```
- Установить зависимости
```
pip install -r requirements.txt
```
- Запустить тесты обязательно указав параметр "--language"
```
pytest -s -v --language=fr test_items.py #по умолчанию запускается Chrome
pytest -s -v --language=ru --browser_name=firefox test_items.py #запустится firefox
```

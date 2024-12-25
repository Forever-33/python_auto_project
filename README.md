# Тестирование сервиса https://www.saucedemo.com (pytest+selenium+allure)

### ```./base/basepage.py``` - Описание методов взаимодействия с базовой страницей
### ```./base/pages``` - Директория с описанием взаимодействия методов с каждой тестируемой страницей
### ```./config/base_test.py``` - Использование классов страниц для тестов
### ```./config/base_test.py``` - Директория с тестами
### ```./conftest.py``` - Настройка и конфигурация тестов
### ```./requirements.txt``` - Используемые пакеты в проекте

#### Установка зависимостей
``` 
pip install -r requirements.txt
```

#### Запуск тестов и генерация allure отчетности
``` 
pytest -v --alluredir=./allure-results
```

#### Запуск allure отчета
``` 
allure serve ./allure-results  
```
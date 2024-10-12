# Проект "Test_poetry"

## Описание:

Виджет, который показывает несколько последних успешных банковских операций клиента

## Установка:

1. Клонируйте репозиторий:
```
git clone https://github.com/VVELDI/python_homework1.git
```

2. Установите зависимости:
```
pip install -r requirements.txt
```
## Использование:

Реализовано несколько функций:

**mask_account_card** - Обрабатывает и маскирует информацию о картах и о счетах
```
# Пример для карты
Visa Platinum 7000792289606361  # входной аргумент
Visa Platinum 7000 79** **** 6361  # выход функции

# Пример для счета
Счет 73654108430135874305  # входной аргумент
Счет **4305  # выход функции
```

**get_date** - Приводит дату к формату "ДД.ММ.ГГГГ"
```
Принимает на вход строку с датой в формате 
"2024-03-11T02:26:18.671407"
 и возвращает строку с датой в формате 
"11.03.2024"
```


**filter_by_state** - Принимает список словарей и опционально значение для ключа.
Функция возвращает новый список словарей, содержащий только те словари, у которых ключ
"state" соответствует указанному значению

**Пример входных данных:**
```
[{'id': 41428829, 'state': 'EXECUTED', 'date': '2019-07-03T18:35:29.512364'}, {'id': 939719570, 'state': 'EXECUTED', 'date': '2018-06-30T02:08:58.425572'}, {'id': 594226727, 'state': 'CANCELED', 'date': '2018-09-12T21:27:25.241689'}, {'id': 615064591, 'state': 'CANCELED', 'date': '2018-10-14T08:21:33.419441'}]
```
 Выход функции со статусом по умолчанию 'EXECUTED'
 ```
[{'id': 41428829, 'state': 'EXECUTED', 'date': '2019-07-03T18:35:29.512364'}, {'id': 939719570, 'state': 'EXECUTED', 'date': '2018-06-30T02:08:58.425572'}]
```
 Выход функции, если вторым аргументов передано 'CANCELED'
```
[{'id': 594226727, 'state': 'CANCELED', 'date': '2018-09-12T21:27:25.241689'}, {'id': 615064591, 'state': 'CANCELED', 'date': '2018-10-14T08:21:33.419441'}]
```
**sort_by_date** - Принимает список словарей и необязательный параметр, задающий порядок сортировки
(по умолчанию — убывание). Функция должна возвращать новый список, отсортированный по дате
```
(сортировка по убыванию, т. е. сначала самые последние операции)
[{'id': 41428829, 'state': 'EXECUTED', 'date': '2019-07-03T18:35:29.512364'}, {'id': 615064591, 'state': 'CANCELED', 'date': '2018-10-14T08:21:33.419441'}, {'id': 594226727, 'state': 'CANCELED', 'date': '2018-09-12T21:27:25.241689'}, {'id': 939719570, 'state': 'EXECUTED', 'date': '2018-06-30T02:08:58.425572'}]

```

### Генераторы

В модуле **src\generators.py** написаны следующие генераторы:
***filter_by_currency*** - `Принимает на вход список словарей, представляющих транзакции,
       возвращает итератор, который поочередно выдает транзакции,
       где валюта операции соответствует заданной (например, USD)`

На входе:
```
[
        {
            "id": 939719570,
            "state": "EXECUTED",
            "date": "2018-06-30T02:08:58.425572",
            "operationAmount": {
                "amount": "9824.07",
                "currency": {
                    "name": "USD",
                    "code": "USD"
                }
            },
            "description": "Перевод организации",
            "from": "Счет 75106830613657916952",
            "to": "Счет 11776614605963066702"
        },
        {
            "id": 142264268,
            "state": "EXECUTED",
            "date": "2019-04-04T23:20:05.206878",
            "operationAmount": {
                "amount": "79114.93",
                "currency": {
                    "name": "USD",
                    "code": "USD"
                }
            },
            "description": "Перевод со счета на счет",
            "from": "Счет 19708645243227258542",
            "to": "Счет 75651667383060284188"
        },
        {
            "id": 873106923,
            "state": "EXECUTED",
            "date": "2019-03-23T01:09:46.296404",
            "operationAmount": {
                "amount": "43318.34",
                "currency": {
                    "name": "руб.",
                    "code": "RUB"
                }
            },
            "description": "Перевод со счета на счет",
            "from": "Счет 44812258784861134719",
            "to": "Счет 74489636417521191160"
        },
        {
            "id": 895315941,
            "state": "EXECUTED",
            "date": "2018-08-19T04:27:37.904916",
            "operationAmount": {
                "amount": "56883.54",
                "currency": {
                    "name": "USD",
                    "code": "USD"
                }
            },
            "description": "Перевод с карты на карту",
            "from": "Visa Classic 6831982476737658",
            "to": "Visa Platinum 8990922113665229"
        },
        {
            "id": 594226727,
            "state": "CANCELED",
            "date": "2018-09-12T21:27:25.241689",
            "operationAmount": {
                "amount": "67314.70",
                "currency": {
                    "name": "руб.",
                    "code": "RUB"
                }
            },
            "description": "Перевод организации",
            "from": "Visa Platinum 1246377376343588",
            "to": "Счет 14211924144426031657"
        }
    ]

```
На выходе:
```
# при первой итерации

{'id': 939719570,
'state': 'EXECUTED',
'date': '2018-06-30T02:08:58.425572',
'operationAmount': {'amount': '9824.07',
                  'currency': {'name': 'USD', 'code': 'USD'}},
'description': 'Перевод организации',
'from': 'Счет 75106830613657916952',
'to': 'Счет 11776614605963066702'}

# при второй итерации

{'id': 142264268,
'state': 'EXECUTED',
'date': '2019-04-04T23:20:05.206878',
'operationAmount': {'amount': '79114.93',
                  'currency': {'name': 'USD', 'code': 'USD'}},
'description': 'Перевод со счета на счет',
'from': 'Счет 19708645243227258542',
'to': 'Счет 75651667383060284188'}
```
***transaction_descriptions*** - `Принимает список словарей с транзакциями и возвращает описание каждой операции по очереди`

На входе:
```
[
        {
            "id": 939719570,
            "state": "EXECUTED",
            "date": "2018-06-30T02:08:58.425572",
            "operationAmount": {
                "amount": "9824.07",
                "currency": {
                    "name": "USD",
                    "code": "USD"
                }
            },
            "description": "Перевод организации",
            "from": "Счет 75106830613657916952",
            "to": "Счет 11776614605963066702"
        },
        {
            "id": 142264268,
            "state": "EXECUTED",
            "date": "2019-04-04T23:20:05.206878",
            "operationAmount": {
                "amount": "79114.93",
                "currency": {
                    "name": "USD",
                    "code": "USD"
                }
            },
            "description": "Перевод со счета на счет",
            "from": "Счет 19708645243227258542",
            "to": "Счет 75651667383060284188"
        },
        {
            "id": 873106923,
            "state": "EXECUTED",
            "date": "2019-03-23T01:09:46.296404",
            "operationAmount": {
                "amount": "43318.34",
                "currency": {
                    "name": "руб.",
                    "code": "RUB"
                }
            },
            "description": "Перевод со счета на счет",
            "from": "Счет 44812258784861134719",
            "to": "Счет 74489636417521191160"
        }
]
```
На выходе:
```
# При первой итерации:
"Перевод организации"

#При второй итерации:
"Перевод со счета на счет"

#При второй итерации
"Перевод со счета на счет"
```

***card_number_generator*** - `Выдает номера банковских карт. Генератор может сгенерировать номера карт в заданном диапазоне.
    На входе начальное и конечное значение, на выходе - номер карты`

Пример: на входе 5 - начальное значение, 7 - конечное значение:
```
# При первой итерации
0000 0000 0000 0005

# При второй итерации
0000 0000 0000 0006
# При третьей итерации
0000 0000 0000 0007
```
### Декораторы

В модуле ***decorators.py*** - реализован декоратор log, `который записывает в лог результат функции,
а также ее начало выполнения и конец. Если функция завершилась с ошибкой, то это тоже записывается в лог,
с указанием ошибки и аргументами, которые были использованы при вызове ошибки.`

Если при вызове декоратора log(), указать в его аргументе название файлы, наприме `@log("log.txt")` - 
то в рабочей директории создастся файл `log.txt`, в который будет записываться лог. `Если не указывать название файла -
весь лог будет записываться в консоль`
### Тесты

В директории **\tests** лежат тесты для каждой функции программы по-модульно,
оставлены комментарии для каждого теста. 

Для запуска тестов необходимо установить фреймворк pytest, и прописать в терминале команду pytest

```
# Установка через Poetry
poetry add --group dev pytest

#Для запуска 
pytest
```
В модуле **conftest.py** хранятся фикстуры для тестов.

В папке **\htmlcov** находится html файлы с процентом покрытия тестами.



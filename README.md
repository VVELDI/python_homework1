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



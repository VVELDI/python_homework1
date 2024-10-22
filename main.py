import os
from src import generators, processing, transaction_parser, utils

project_root = os.path.dirname(os.path.abspath(__file__))

# Путь к директории с данными
data_dir = os.path.join(project_root, 'data')

# Создаем переменные для различных файлов
json_file_path = os.path.join(data_dir, 'operations.json')
csv_file_path = os.path.join(data_dir, 'transactions.csv')
html_file_path = os.path.join(data_dir, 'transactions_excel.xlsx')

# Создаем параметры по умолчанию
default_parameters = {
    "reverse_flag": True
}
set_of_acceptable_status = ['EXECUTED', 'CANCELED', 'PENDING']

# Словарь для ответа на ввод пользователя
file_type_massages = {
    1: "Для обработки выбран JSON-файл\n",
    2: "Для обработки выбран CSV-файл\n",
    3: "Для обработки выбран XLSX-файл\n"
}

flag = True

print(f'''Привет! Добро пожаловать в программу работы 
с банковскими транзакциями. 
Выберите необходимый пункт меню:\n''')

while flag:
    try:
        operation_number = int(input("1. Получить информацию о транзакциях из JSON-файла\n"
                                     "2. Получить информацию о транзакциях из CSV-файла\n"
                                     "3. Получить информацию о транзакциях из XLSX-файла\n"))

        if operation_number not in [1, 2, 3]:
            print('Введите значение от 1 до 3\n')
        else:
            flag = False
    except ValueError:
        print('Введите значение от 1 до 3\n')

if operation_number == 1:
    list_transactions = utils.load_transactions_from_json(json_file_path)
elif operation_number == 2:
    list_transactions = transaction_parser.read_transactions_from_csv(csv_file_path)
else:
    list_transactions = transaction_parser.read_transactions_from_excel(html_file_path)

print(file_type_massages[operation_number])


# Печать общего количества транзакций
total_transactions = len(list_transactions)

if total_transactions == 0:
    print("Программа: Не найдено ни одной транзакции, подходящей под ваши условия фильтрации.")
else:
    flag = True
    while flag:
        state = input("Введите статус, по которому необходимо выполнить фильтрацию.\n"
                      "Доступные для фильтровки статусы: EXECUTED, CANCELED, PENDING\n").upper()
        if state not in set_of_acceptable_status:
            print(f'Статус операции "{state}" недоступен.')
        else:
            flag = False

    sorted_list_transactions = processing.filter_by_state(list_transactions, state)

    # Печать количества транзакций после фильтрации по статусу
    filtered_transactions_count = len(sorted_list_transactions)

    if filtered_transactions_count == 0:
        print("Программа: Не найдено ни одной транзакции, подходящей под ваши условия фильтрации.")
    else:
        sorting_value = input("Отсортировать операции по дате? Да/Нет\n")
        if sorting_value.lower() == "да":
            revers_flag_value = input('Отсортировать по "возрастанию" или по "убыванию?"\n')
            default_parameters['reverse_flag'] = (revers_flag_value.lower() != "возрастанию")
            sorted_list_transactions = processing.sort_by_date(sorted_list_transactions, default_parameters['reverse_flag'])

        # Запрос фильтрации по валюте
        request_for_withdrawal_in_currency = input('Выводить только рублевые транзакции? Да/Нет\n')
        if request_for_withdrawal_in_currency.lower() == 'да':
            currency = "RUB"
            filtering_by_rub = list(generators.filter_by_currency(sorted_list_transactions, currency))
            sorted_list_transactions = filtering_by_rub

        # Проверка на пустоту списка после фильтрации
        if not sorted_list_transactions:
            print("Программа: Не найдено ни одной транзакции, подходящей под ваши условия фильтрации.")
        else:
            # Запрос фильтрации по описанию
            request_for_filtration = input('Отфильтровать список транзакций по определенному слову в описании? Да/Нет\n')
            if request_for_filtration.lower() == 'да':
                search_str = input('Введите это слово: ')
                result_list_transactions = processing.filter_transactions_by_description(sorted_list_transactions, search_str)

                # Проверка на пустоту после фильтрации
                if not result_list_transactions:
                    print(f"Программа: Не найдено ни одной транзакции, подходящей под слово '{search_str}' в описании.")
                else:
                    print('Распечатываю итоговый список транзакций...\n')
                    print(f"Всего банковских операций в выборке: {len(result_list_transactions)}")
                    print(result_list_transactions)
            else:
                print('Распечатываю итоговый список транзакций...\n')
                print(f"Всего банковских операций в выборке: {len(sorted_list_transactions)}")
                print(sorted_list_transactions)

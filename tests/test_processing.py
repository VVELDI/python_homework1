import pytest
from collections import Counter
import src.processing


@pytest.mark.parametrize("data_dictionary, state_, expected", [
    ([{'id': 41428829, 'state': 'EXECUTED', 'date': '2019-07-03T18:35:29.512364'},  # если state_ отличается от
      {'id': 939719570, 'state': 'EXECUTED', 'date': '2018-06-30T02:08:58.425572'}],  # EXECUTED или 'CANCELED'
     'qwe',  # вернет []
     []),
    ([{'id': 594226727, 'date': '2018-09-12T21:27:25.241689'}],
     "",
     [])
])
def test_filter_by_state(data_dictionary, state_, expected):
    assert src.processing.filter_by_state(data_dictionary, state_) == expected


def test_with_state_executed(default_test_list):
    assert src.processing.filter_by_state(default_test_list, "EXECUTED") == [{'id': 41428829,
                                                                              'state': 'EXECUTED',
                                                                              'date': '2019-07-03T18:35:29.512364'},
                                                                             {'id': 939719570, 'state': 'EXECUTED',
                                                                              'date': '2018-06-30T02:08:58.425572'}]


def test_with_state_canceled(default_test_list):
    assert src.processing.filter_by_state(default_test_list, "CANCELED") == [{'id': 594226727,
                                                                              'state': 'CANCELED',
                                                                              'date': '2018-09-12T21:27:25.241689'},
                                                                             {'id': 615064591, 'state': 'CANCELED',
                                                                              'date': '2018-10-14T08:21:33.419441'}]


@pytest.mark.parametrize("data_dictionary, reverse_flag, expected", [
    ([{'id': 41428829, 'state': 'EXECUTED', 'date': '2019-07-03T18:35:29.512364'},  # для одинаковых date
      {'id': 594226727, 'state': 'CANCELED', 'date': '2018-09-12T21:27:25.241689'},
      {'id': 939719570, 'state': 'EXECUTED', 'date': '2019-07-03T18:35:29.512364'}],
     True,
     [{'id': 41428829, 'state': 'EXECUTED', 'date': '2019-07-03T18:35:29.512364'},
      {'id': 939719570, 'state': 'EXECUTED', 'date': '2019-07-03T18:35:29.512364'},
      {'id': 594226727, 'state': 'CANCELED', 'date': '2018-09-12T21:27:25.241689'},
      ]),
    ([{'id': 41428829, 'state': 'EXECUTED', 'date': '2012.07.03'},  # для нестандартных дат
      {'id': 594226727, 'state': 'CANCELED', 'date': '2018-09-12T21:27:25.241689'},
      {'id': 939719570, 'state': 'EXECUTED', 'date': '2019-07-03T18:35:29.512364'}],
     True,
     [{'id': 41428829, 'state': 'EXECUTED', 'date': 'Формат даты неверный: 2012.07.03'},
      {'id': 939719570, 'state': 'EXECUTED', 'date': '2019-07-03T18:35:29.512364'},
      {'id': 594226727, 'state': 'CANCELED', 'date': '2018-09-12T21:27:25.241689'},
      ]),
    ([{'id': 41428829, 'state': 'EXECUTED', 'date': '07.03'},  # для некорректных дат
      {'id': 594226727, 'state': 'CANCELED', 'date': '2018-09-12T21:27:25.241689'},
      {'id': 939719570, 'state': 'EXECUTED', 'date': '2019-07-03T18:35:29.512364'}],
     True,
     [{'id': 41428829, 'state': 'EXECUTED', 'date': 'Формат даты неверный: 07.03'},
      {'id': 939719570, 'state': 'EXECUTED', 'date': '2019-07-03T18:35:29.512364'},
      {'id': 594226727, 'state': 'CANCELED', 'date': '2018-09-12T21:27:25.241689'},
      ]),
    ([{'id': 41428829, 'state': 'EXECUTED', 'date': '07.03'},  # для некорректного значения ключа
      {'id': 594226727, 'state': 'CANCELED', 'dat': '2018-09-12T21:27:25.241689'}],
     True,
     ["Список не корректен, в одной/нескольких словарях отсутствует ключ 'date'"])
])
def test_sort_by_date(data_dictionary, reverse_flag, expected):
    assert src.processing.sort_by_date(data_dictionary, reverse_flag) == expected


# Тест с флагом по умолчанию True
def test_sort_with_true(default_test_list):
    assert src.processing.sort_by_date(default_test_list, True) == [{'id': 41428829, 'state': 'EXECUTED',
                                                                     'date': '2019-07-03T18:35:29.512364'},
                                                                    {'id': 615064591, 'state': 'CANCELED',
                                                                     'date': '2018-10-14T08:21:33.419441'},
                                                                    {'id': 594226727, 'state': 'CANCELED',
                                                                     'date': '2018-09-12T21:27:25.241689'},
                                                                    {'id': 939719570, 'state': 'EXECUTED',
                                                                     'date': '2018-06-30T02:08:58.425572'}]


# Тест с флагом по умолчанию False
def test_sort_with_false(default_test_list):
    assert src.processing.sort_by_date(default_test_list, False) == [{'id': 939719570,
                                                                      'state': 'EXECUTED',
                                                                      'date': '2018-06-30T02:08:58.425572'},
                                                                     {'id': 594226727, 'state': 'CANCELED',
                                                                      'date': '2018-09-12T21:27:25.241689'},
                                                                     {'id': 615064591, 'state': 'CANCELED',
                                                                      'date': '2018-10-14T08:21:33.419441'},
                                                                     {'id': 41428829, 'state': 'EXECUTED',
                                                                      'date': '2019-07-03T18:35:29.512364'}]

def test_filter_transactions_by_description():
    transactions = [
        {'id': 1, 'description': 'Перевод со счета на счет'},
        {'id': 2, 'description': 'Покупка в магазине'},
        {'id': 3, 'description': 'Заработная плата'},
        {'id': 4, 'description': 'Перевод на карту'},
        {'id': 5, 'description': 'Платеж за коммунальные услуги'}
    ]

    # Тест: поиск слова "Перевод"
    result = src.processing.filter_transactions_by_description(transactions, "Перевод")
    expected = [
        {'id': 1, 'description': 'Перевод со счета на счет'},
        {'id': 4, 'description': 'Перевод на карту'}
    ]
    assert result == expected

    # Тест: поиск слова "платеж"
    result = src.processing.filter_transactions_by_description(transactions, "платеж")
    expected = [
        {'id': 5, 'description': 'Платеж за коммунальные услуги'}
    ]
    assert result == expected

    # Тест: поиск слова, которого нет в списке
    result = src.processing.filter_transactions_by_description(transactions, "нет такого слова")
    expected = []
    assert result == expected

    # Тест: поиск пустой строки
    result = src.processing.filter_transactions_by_description(transactions, "")
    expected = transactions  # Возвращает все транзакции
    assert result == expected

    # Тест: поиск с учетом регистра
    result = src.processing.filter_transactions_by_description(transactions, "заработная")
    expected = [
        {'id': 3, 'description': 'Заработная плата'}
    ]
    assert result == expected


def test_count_operations_by_category():
    transactions = [
        {'id': 1, 'description': 'Покупка в магазине'},
        {'id': 2, 'description': 'Перевод на счет'},
        {'id': 3, 'description': 'Оплата счета'},
        {'id': 4, 'description': 'Покупка в магазине'},
        {'id': 5, 'description': 'Заработная плата'},
        {'id': 6, 'description': 'Перевод на счет'},
        {'id': 7, 'description': 'Оплата счета'},
        {'id': 8, 'description': 'Покупка в аптеке'}
    ]

    categories = ['Покупка в магазине', 'Оплата счета', 'Перевод на счет']

    # Тест: количество операций по указанным категориям
    result = src.processing.count_operations_by_category(transactions, categories)
    expected = {
        'Покупка в магазине': 2,
        'Оплата счета': 2,
        'Перевод на счет': 2
    }
    assert result == expected

    # Тест: отсутствие операций по категориям
    result = src.processing.count_operations_by_category(transactions, ['неизвестная категория'])
    expected = {}
    assert result == expected

    # Тест: некоторые категории отсутствуют в транзакциях
    result = src.processing.count_operations_by_category(transactions, ['Покупка в магазине', 'неизвестная категория'])
    expected = {
        'Покупка в магазине': 2
    }
    assert result == expected

    # Тест: пустой список транзакций
    result = src.processing.count_operations_by_category([], categories)
    expected = {}
    assert result == expected

    # Тест: пустой список категорий
    result = src.processing.count_operations_by_category(transactions, [])
    expected = {}
    assert result == expected

    def test_count_operations_by_category_success():
        transactions = [
            {'description': 'Payment'},
            {'description': 'Transfer'},
            {'description': 'Payment'},
            {'description': 'Refund'},
            {'description': 'Transfer'},
            {'description': 'Withdrawal'}
        ]
        categories = ['Payment', 'Transfer', 'Refund']

        result = src.processing.count_operations_by_category(transactions, categories)

        # Ожидаемый результат: Payment - 2, Transfer - 2, Refund - 1
        assert result == {
            'Payment': 2,
            'Transfer': 2,
            'Refund': 1
        }

    def test_count_operations_by_category_no_match():
        transactions = [
            {'description': 'Payment'},
            {'description': 'Transfer'},
            {'description': 'Refund'}
        ]
        categories = ['Withdrawal', 'Deposit']

        result = src.processing.count_operations_by_category(transactions, categories)

        # Ожидаем пустой словарь, так как нет совпадений с категориями
        assert result == {}

    def test_count_operations_by_category_empty_transactions():
        transactions = []
        categories = ['Payment', 'Transfer']

        result = src.processing.count_operations_by_category(transactions, categories)

        # Ожидаем пустой словарь, так как нет транзакций
        assert result == {}

    def test_count_operations_by_category_duplicate_categories():
        transactions = [
            {'description': 'Payment'},
            {'description': 'Payment'},
            {'description': 'Transfer'},
            {'description': 'Payment'}
        ]
        categories = ['Payment', 'Transfer']

        result = src.processing.count_operations_by_category(transactions, categories)

        # Ожидаемый результат: Payment - 3, Transfer - 1
        assert result == {
            'Payment': 3,
            'Transfer': 1
        }

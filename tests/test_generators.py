import pytest

import src.generators


def test_filter_by_currency(default_transactions, transactions_are_free_of_currency):
    filtered_transactions_by_usd = (src.generators.filter_by_currency(default_transactions, "USD"))
    filtered_transactions_by_rub = (src.generators.filter_by_currency(default_transactions, "RUB"))

    # Incorrect transactions
    filter_by_wrong_currency_1 = src.generators.filter_by_currency(transactions_are_free_of_currency, "RUB")
    filter_by_wrong_currency_2 = src.generators.filter_by_currency(default_transactions, "")
    filter_by_wrong_currency_3 = src.generators.filter_by_currency([], "RUB")
    assert next(filtered_transactions_by_usd) == {'id': 939719570,
                                                  'state': 'EXECUTED',
                                                  'date': '2018-06-30T02:08:58.425572',
                                                  'operationAmount': {'amount': '9824.07',
                                                                      'currency': {'name': 'USD', 'code': 'USD'}},
                                                  'description': 'Перевод организации',
                                                  'from': 'Счет 75106830613657916952',
                                                  'to': 'Счет 11776614605963066702'}
    assert next(filtered_transactions_by_usd) == {'id': 142264268,
                                                  'state': 'EXECUTED',
                                                  'date': '2019-04-04T23:20:05.206878',
                                                  'operationAmount': {'amount': '79114.93',
                                                                      'currency': {'name': 'USD', 'code': 'USD'}},
                                                  'description': 'Перевод со счета на счет',
                                                  'from': 'Счет 19708645243227258542',
                                                  'to': 'Счет 75651667383060284188'}

    assert next(filtered_transactions_by_rub) == {'id': 873106923, 'state': 'EXECUTED',
                                                  'date': '2019-03-23T01:09:46.296404',
                                                  'operationAmount': {'amount': '43318.34',
                                                                      'currency': {'name': 'руб.', 'code': 'RUB'}},
                                                  'description': 'Перевод со счета на счет',
                                                  'from': 'Счет 44812258784861134719',
                                                  'to': 'Счет 74489636417521191160'}

    assert next(filtered_transactions_by_rub) == {'id': 594226727, 'state': 'CANCELED',
                                                  'date': '2018-09-12T21:27:25.241689',
                                                  'operationAmount': {'amount': '67314.70',
                                                                      'currency': {'name': 'руб.', 'code': 'RUB'}},
                                                  'description': 'Перевод организации',
                                                  'from': 'Visa Platinum 1246377376343588',
                                                  'to': 'Счет 14211924144426031657'}

    with pytest.raises(StopIteration) as exc_info:
        print(next(filter_by_wrong_currency_1))
    assert str(exc_info.value) == "Транзакции отсутствуют"

    with pytest.raises(StopIteration) as exc_info:
        print(next(filter_by_wrong_currency_2))
    assert str(exc_info.value) == "Транзакции в заданной валюте отсутствуют"

    with pytest.raises(StopIteration) as exc_info:
        print((next(filter_by_wrong_currency_3)))
    assert str(exc_info.value) == "Транзакции отсутствуют"


def test_transaction_descriptions(default_transactions, transactions_are_free_of_currency):
    correct_descriptions = src.generators.transaction_descriptions(default_transactions)
    no_description = src.generators.transaction_descriptions(transactions_are_free_of_currency)
    for i, transactions in enumerate(default_transactions):                # Проверка на правильную
        assert next(correct_descriptions) == transactions["description"]   # итерацию

    assert next(no_description) == "Описания нет"            # Проверка на отсутствие ключа в списке словарей


@pytest.mark.parametrize("initial_value, final_value", [(9999, 10002)])
def test_card_number_generator(initial_value, final_value):
    card_number = src.generators.card_number_generator(initial_value, final_value)
    assert (next(card_number)) == "0000 0000 0000 9999"
    assert (next(card_number)) == "0000 0000 0001 0000"
    assert (next(card_number)) == "0000 0000 0001 0001"
    assert (next(card_number)) == "0000 0000 0001 0002"


def test_card_number_generator_beyond_the_iteration():
    card_number_beyond_the_iteration = src.generators.card_number_generator(1, 2)
    card_number_invalid_range = src.generators.card_number_generator(9999999999999999, 10000000000000000)
    assert (next(card_number_beyond_the_iteration)) == "0000 0000 0000 0001"
    assert (next(card_number_beyond_the_iteration)) == "0000 0000 0000 0002"
    with pytest.raises(StopIteration) as exc_info:
        print(next(card_number_beyond_the_iteration))
    assert str(exc_info.value) == "Выход за пределы генерации"
    with pytest.raises(StopIteration) as exc_info:
        print(next(card_number_invalid_range))
    assert str(exc_info.value) == "Указанные значения выходят за предел диапазона"

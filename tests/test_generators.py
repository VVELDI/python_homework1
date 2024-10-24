import pytest

import src.generators


def test_filter_by_currency_success():
    transactions = [
        {'operationAmount': {'currency': {'code': 'USD'}, 'amount': '100.00'}, 'description': 'Payment'},
        {'operationAmount': {'currency': {'code': 'EUR'}, 'amount': '200.00'}, 'description': 'Transfer'},
        {'currency_code': 'USD', 'amount': '300.00', 'description': 'Purchase'},
    ]

    # Фильтруем транзакции по USD
    result = src.generators.filter_by_currency(transactions, "USD")

    # Проверяем, что возвращаются только транзакции с USD
    assert next(result) == {'operationAmount': {'currency': {'code': 'USD'}, 'amount': '100.00'},
                            'description': 'Payment'}
    assert next(result) == {'currency_code': 'USD', 'amount': '300.00', 'description': 'Purchase'}

    # Проверяем, что больше транзакций нет и вызов next поднимет StopIteration
    with pytest.raises(StopIteration):
        next(result)


def test_filter_by_currency_not_found():
    transactions = [
        {'operationAmount': {'currency': {'code': 'EUR'}, 'amount': '100.00'}, 'description': 'Payment'},
        {'currency_code': 'RUB', 'amount': '300.00', 'description': 'Purchase'}
    ]

    # Фильтруем транзакции по USD, которых нет
    result = src.generators.filter_by_currency(transactions, "USD")

    # Ожидаем сообщение о том, что транзакции с такой валютой отсутствуют
    assert next(result) == "Транзакции в заданной валюте отсутствуют"

    # Проверяем, что больше нет транзакций и поднят StopIteration
    with pytest.raises(StopIteration):
        next(result)


def test_filter_by_currency_incorrect_data():
    transactions = [
        {'operationAmount': {'amount': '100.00'}, 'description': 'Payment'},  # Отсутствует currency
        {'description': 'Purchase'}  # Нет currency_code и operationAmount
    ]

    # Фильтруем транзакции по USD
    result = src.generators.filter_by_currency(transactions, "USD")

    # Ожидаем сообщение о том, что транзакции с такой валютой отсутствуют
    assert next(result) == "Транзакции в заданной валюте отсутствуют"

    # Проверяем, что больше нет транзакций и поднят StopIteration
    with pytest.raises(StopIteration):
        next(result)


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

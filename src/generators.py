def filter_by_currency(transactions: list, currency: str) -> list:
    """Принимает на вход список словарей, представляющих транзакции,
       возвращает итератор, который поочередно выдает транзакции,
       где валюта операции соответствует заданной (например, USD)"""
    if not transactions or len(transactions) == 0:
        return "Транзакции отсутствуют"
    flag = 0
    for transaction in transactions:
        try:
            if transaction['operationAmount']['currency']['code'] == currency:
                yield transaction
            else:
                flag += 1
        except KeyError:
            return "Транзакции отсутствуют"
    if flag == len(transactions):
        return "Транзакции в заданной валюте отсутствуют"


# filtered_transactions = (filter_by_currency(transaction, "Валюта")) - для дальнейшего использования


def transaction_descriptions(transactions: list) -> str:
    """Принимает список словарей с транзакциями и возвращает описание каждой операции по очереди"""
    for transaction in transactions:
        try:
            if transaction["description"]:
                yield transaction["description"]
        except KeyError:
            yield "Описания нет"


# descriptions = transaction_descriptions(transactions) - для дальнейшего использования


def card_number_generator(initial_value: int, final_value: int) -> str:
    """Выдает номера банковских карт. Генератор может сгенерировать номера карт в заданном диапазоне.
    На входе начальное и конечное значение, на выходе - номер карты"""
    if 1 > initial_value or initial_value > 9999999999999999 or final_value < 1 or final_value > 9999999999999999:
        return "Указанные значения выходят за предел диапазона"
    while initial_value <= final_value:
        list_of_numbers_card = [0 for x in range(16)]
        list_of_numbers_card.append(initial_value)
        for i in range(len(str(initial_value))):
            del list_of_numbers_card[i]
        card_digits = "".join(map(str, list_of_numbers_card))
        card_number = card_digits[0:4] + " " + card_digits[4:8] + " " + card_digits[8:12] + " " + card_digits[12:16]
        yield card_number
        initial_value += 1
    return "Выход за пределы генерации"

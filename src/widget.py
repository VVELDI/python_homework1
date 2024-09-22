import datetime
from src import masks


def mask_account_card(card: str) -> str:
    """Обрабатывает информацию о картах и о счетах"""
    index_of_the_card = 0
    for i in range(len(card), 0, -1):
        if card[i - 1].isdigit():
            continue
        else:
            index_of_the_card = i
            break
    if "Счет" in card:
        if masks.get_mask_account(card[index_of_the_card: len(card)]) == "Данные не корректны":
            return "Данные не корректны"
        else:
            mask_number = "Счет " + masks.get_mask_account(card[index_of_the_card: len(card)])
    else:
        if masks.get_mask_card_number(card[index_of_the_card: len(card)+1]) == "Данные не корректны":
            return "Данные не корректны"
        else:
            mask_number = card[0: index_of_the_card] + masks.get_mask_card_number(card[index_of_the_card: len(card)+1])
    return mask_number


def get_date(date: str) -> str:
    """Приводит дату к формату ДД.ММ.ГГГГ"""
    return datetime.datetime.strptime(date, "%Y-%m-%dT%H:%M:%S.%f").strftime("%d.%m.%Y")


print(mask_account_card("Счет 73654108430135874305"))

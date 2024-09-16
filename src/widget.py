import masks
import datetime


def mask_account_card(card: str) -> str:
    """Обрабатывает информацию о картах и о счетах"""
    index_of_the_card = 0
    for i in range(len(card), 0, -1):
        if card[i - 1].isdigit():
            continue
        else:
            index_of_the_card = i - 1
            break
    if "Счет" in card:
        mask_number = "Счет " + masks.get_mask_account(card[index_of_the_card:len(card)])
    else:
        mask_number = card[0:index_of_the_card + 1] + masks.get_mask_card_number(card[index_of_the_card + 1:len(card)])
    return mask_number


def get_date(date: str) -> str:
    return datetime.datetime.strptime(date, "%Y-%m-%dT%H:%M:%S.%f").strftime("%d.%m.%Y")

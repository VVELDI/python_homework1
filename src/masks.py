def get_mask_card_number(card_number: str) -> str:
    """Принимает на вход номер карты и возвращает ее маску."""
    new_card_number = []
    mask_card_number = []
    for index, digit in enumerate(card_number):
        if index not in [6, 7, 8, 9, 10, 11]:
            new_card_number.append(digit)
        else:
            new_card_number.append("*")

    for index, symbol in enumerate(new_card_number):
        if index not in [4, 9, 14]:
            mask_card_number.append(symbol)
        else:
            mask_card_number.append(" ")
            mask_card_number.append(symbol)

    return "".join(mask_card_number)


def get_mask_account(account_number: str) -> str:
    """Принимает на вход номер счета и возвращает его маску."""
    new_account_number = []
    for index in range(-6, 0):
        if index in [-6, -5]:
            new_account_number.append("*")
        else:
            new_account_number.append(account_number[index])

    return "".join(new_account_number)

import logging
import os

# Настройка логирования
log_dir = 'logs'
if not os.path.exists(log_dir):
    os.makedirs(log_dir)

log_file = os.path.join(log_dir, 'masks.log')

# Создаем обработчик файла с указанием кодировки и режимом 'w' для перезаписи
file_handler = logging.FileHandler(log_file, mode='w', encoding='utf-8')
file_handler.setLevel(logging.INFO)

# Формат логирования: [время] [модуль] [уровень] [сообщение]
formatter = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s')
file_handler.setFormatter(formatter)

# Настройка основного логгера
logger = logging.getLogger("masks")
logger.setLevel(logging.INFO)
logger.addHandler(file_handler)


def get_mask_card_number(card_number: str) -> str:
    """Принимает на вход номер карты и возвращает ее маску."""
    logger.info('Функция get_mask_card_number была вызвана с аргументом: %s', card_number)

    if len(card_number) != 16 or not card_number.isdigit():
        logger.error("Некорректные данные для карты: %s", card_number)
        return "Данные не корректны"

    new_card_number = []
    mask_card_number = []
    for index, digit in enumerate(card_number):
        if index not in [6, 7, 8, 9, 10, 11]:
            new_card_number.append(digit)
        else:
            new_card_number.append("*")

    for index, symbol in enumerate(new_card_number):
        if index not in [4, 8, 12]:
            mask_card_number.append(symbol)
        else:
            mask_card_number.append(" ")
            mask_card_number.append(symbol)

    masked = "".join(mask_card_number)
    logger.info('Маскированный номер карты: %s', masked)
    return masked


def get_mask_account(account_number: str) -> str:
    """Принимает на вход номер счета и возвращает его маску."""
    logger.info('Функция get_mask_account была вызвана с аргументом: %s', account_number)

    if len(account_number) != 20 or not account_number.isdigit():
        logger.error("Некорректные данные для счета: %s", account_number)
        return "Данные не корректны"

    new_account_number = []
    for index in range(-6, 0):
        if index in [-6, -5]:
            new_account_number.append("*")
        else:
            new_account_number.append(account_number[index])

    masked_account = "".join(new_account_number)
    logger.info('Маскированный номер счета: %s', masked_account)
    return masked_account


print(get_mask_card_number("9999999999999999"))
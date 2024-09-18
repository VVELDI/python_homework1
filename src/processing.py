from typing import Optional


def filter_by_state(data_dictionary: list, state: Optional[list] = "EXECUTED") -> list:
    """Принимает список словарей и опционально значение для ключа.
    Функция возвращает новый список словарей, содержащий только те словари, у которых ключ
    state соответствует указанному значению
    """
    filtering_by_state = []
    for dictionary in data_dictionary:
        if dictionary['state'] == state:
            filtering_by_state.append(dictionary)
    return filtering_by_state


def sort_by_date(data_dictionary: list, reverse_flag: bool = True) -> list:
    """Принимает список словарей и необязательный параметр, задающий порядок сортировки
    (по умолчанию — убывание). Функция должна возвращать новый список, отсортированный по дате
    """

    data_dictionary.sort(key=lambda dictionary: dictionary['date'], reverse=reverse_flag)
    return data_dictionary


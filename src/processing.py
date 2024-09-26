from typing import Optional

import src.widget


def filter_by_state(data_dictionary: list, state: Optional[list] = "EXECUTED") -> list:
    """Принимает список словарей и опционально значение для ключа.
    Функция возвращает новый список словарей, содержащий только те словари, у которых ключ
    state соответствует указанному значению
    """
    if state not in ['EXECUTED', 'CANCELED']:  # Проверка наличия правильного значения, исключение вернет пустой list
        return []
    else:
        filtering_by_state = []
        for dictionary in data_dictionary:
            if dictionary['state'] == state:
                filtering_by_state.append(dictionary)
        return filtering_by_state


def sort_by_date(data_dictionary: list, reverse_flag: bool = True) -> list:
    """Принимает список словарей и необязательный параметр, задающий порядок сортировки
    (по умолчанию — убывание). Функция должна возвращать новый список, отсортированный по дате
    """
    new_data_dictionary = []
    try:
        for index, data_dict in enumerate(data_dictionary):
            if src.widget.get_date(data_dict["date"]) != "Формат даты неверный":
                new_data_dictionary.append(data_dict)
            else:
                new_data_dictionary.append(data_dict)
                new_data_dictionary[index]['date'] = f"Формат даты неверный: {data_dict['date']}"
    except KeyError:
        return ["Список не корректен, в одной/нескольких словарях отсутствует ключ 'date'"]

    data_dictionary.sort(key=lambda dictionary: dictionary['date'], reverse=reverse_flag)
    return data_dictionary

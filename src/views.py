import json
import os
from datetime import datetime




def get_greeting(current_time: datetime) -> str:
    """
    Определяет приветствие в зависимости от переданного времени суток.

    Аргументы:
    current_time (datetime): Текущее время для определения приветствия.

    Возвращает:
    str: Приветствие ("Доброе утро", "Добрый день", "Добрый вечер", "Доброй ночи").
    """
    current_hour = current_time.hour

    if 5 <= current_hour < 12:
        return "Доброе утро"
    elif 12 <= current_hour < 18:
        return "Добрый день"
    elif 18 <= current_hour < 23:
        return "Добрый вечер"
    else:
        return "Доброй ночи"

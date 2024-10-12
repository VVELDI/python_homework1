import os
import json


def load_transactions_from_json(file_path: str) -> list:
    """
        Загружает данные о транзакциях из JSON-файла. Параметр file_path: Путь до JSON-файла.
        Возвращает список транзакций (список словарей) или пустой список, если файл пустой,
        содержит не список или не найден.
        """
    if not os.path.exists(file_path):
        # Файл не существует
        print(f"Файл {file_path} не найден.")
        return []
    try:
        with open(file_path, 'r', encoding='utf-8') as f:
            data = json.load(f)

        # Проверяем, что данные являются списком
        if isinstance(data, list):
            return data
        else:
            print(f"Содержимое файла {file_path} не является списком.")
            return []

    except json.JSONDecodeError:
        # Ошибка при чтении файла (неверный формат)
        print(f"Файл {file_path} не удалось распознать как JSON.")
        return []

    except Exception as e:
        # Обработка любых других ошибок
        print(f"Произошла ошибка при чтении файла {file_path}: {str(e)}")
        return []


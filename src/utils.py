import json
import os


def load_transactions_from_json(file_path: str) -> list:
    if not os.path.exists(file_path):
        print(f"Файл {file_path} не найден.")
        return []

    try:
        with open(file_path, 'r', encoding='utf-8') as f:
            print("Файл открыт успешно")
            data = json.load(f)
            print("Данные считаны:", data)

        if isinstance(data, list):
            return data
        else:
            print(f"Содержимое файла {file_path} не является списком.")
            return []
    except json.JSONDecodeError:
        print(f"Файл {file_path} не удалось распознать как JSON.")
        return []
    except Exception as e:
        print(f"Произошла ошибка при чтении файла {file_path}: {str(e)}")
        return []

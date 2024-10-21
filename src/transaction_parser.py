import csv

import pandas as pd


def read_transactions_from_csv(file_path: str) -> list:
    """Считывает финансовые операции из CSV-файла и возвращает список словарей с транзакциями."""
    try:
        with open(file_path, mode='r', encoding='utf-8') as csv_file:
            csv_reader = csv.DictReader(csv_file, delimiter=';')
            # Чтение данных и возвращение списка словарей
            return list(csv_reader)
    except FileNotFoundError:
        print(f"Файл {file_path} не найден.")
        return []
    except Exception as e:
        print(f"Ошибка при чтении файла {file_path}: {str(e)}")
        return []


def read_transactions_from_excel(file_path: str) -> list:
    """Считывает финансовые операции из Excel-файла и возвращает список словарей с транзакциями."""
    try:
        # Чтение данных с помощью pandas и преобразование DataFrame в список словарей
        df = pd.read_excel(file_path)
        return df.to_dict(orient='records')
    except FileNotFoundError:
        print(f"Файл {file_path} не найден.")
        return []
    except Exception as e:
        print(f"Ошибка при чтении файла {file_path}: {str(e)}")
        return []

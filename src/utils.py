import logging
import json
import os

# Настройка логирования
log_dir = os.path.join(os.path.dirname(os.path.dirname(__file__)), 'logs')

# Проверяем, существует ли папка logs в корне проекта, если нет - создаем
if not os.path.exists(log_dir):
    os.makedirs(log_dir)

log_file = os.path.join(log_dir, 'utils.log')

# Создаем обработчик файла с указанием кодировки и режимом 'w' для перезаписи
file_handler = logging.FileHandler(log_file, mode='w', encoding='utf-8')
file_handler.setLevel(logging.INFO)

# Формат логирования: [время] [модуль] [уровень] [сообщение]
formatter = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s')
file_handler.setFormatter(formatter)

# Настройка основного логгера
logger = logging.getLogger('utils')
logger.setLevel(logging.INFO)
logger.addHandler(file_handler)


def load_transactions_from_json(file_path: str) -> list:
    logger.info('Функция load_transactions_from_json вызвана с аргументом: %s', file_path)

    if not os.path.exists(file_path):
        logger.error('Файл %s не найден.', file_path)
        print(f"Файл {file_path} не найден.")
        return []

    try:
        with open(file_path, 'r', encoding='utf-8') as f:
            logger.info('Файл открыт успешно: %s', file_path)
            data = json.load(f)
            logger.info('Данные считаны')

        if isinstance(data, list):
            return data
        else:
            logger.error('Содержимое файла %s не является списком.', file_path)
            print(f"Содержимое файла {file_path} не является списком.")
            return []
    except json.JSONDecodeError:
        logger.error('Файл %s не удалось распознать как JSON.', file_path)
        print(f"Файл {file_path} не удалось распознать как JSON.")
        return []
    except Exception as e:
        logger.exception('Произошла ошибка при чтении файла %s: %s', file_path, str(e))
        print(f"Произошла ошибка при чтении файла {file_path}: {str(e)}")
        return []
data_dir = os.path.join(os.path.dirname(os.path.dirname(__file__)), 'data')
file = os.path.join(data_dir, 'operations.json')
print(load_transactions_from_json(file))

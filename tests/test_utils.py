import os
import unittest
from unittest.mock import patch, mock_open
from src.utils import load_transactions_from_json

DATA_DIR = os.path.join(os.path.dirname(__file__), '..', 'data')
JSON_FILE_PATH = os.path.join(DATA_DIR, 'operations.json')


class TestLoadOperations(unittest.TestCase):
    @patch('builtins.open', new_callable=mock_open, read_data='[{"id": 1, "amount": 100}]')
    def test_load_operations_success(self, mock_file):
        # Тест успешной загрузки
        operations = load_transactions_from_json(JSON_FILE_PATH)
        self.assertEqual(len(operations), 1)
        self.assertEqual(operations[0]['id'], 1)

    @patch('builtins.open', new_callable=mock_open, read_data='[]')
    def test_load_operations_empty_file(self, mock_file):
        # Тест для пустого файла
        operations = load_transactions_from_json(JSON_FILE_PATH)
        self.assertEqual(operations, [])

    @patch('builtins.open', side_effect=FileNotFoundError)
    def test_load_operations_file_not_found(self, mock_file):
        # Тест для случая, когда файл не найден
        operations = load_transactions_from_json(JSON_FILE_PATH)
        self.assertEqual(operations, [])

    @patch('builtins.open', new_callable=mock_open, read_data='invalid_json')
    def test_load_operations_invalid_json(self, mock_file):
        # Тест для файла с некорректными данными
        operations = load_transactions_from_json(JSON_FILE_PATH)
        self.assertEqual(operations, [])


if __name__ == '__main__':
    unittest.main()

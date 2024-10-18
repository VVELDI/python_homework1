import unittest
from unittest.mock import mock_open, patch

import pandas as pd

from src.transaction_parser import read_transactions_from_csv, read_transactions_from_excel


class TestCSVReader(unittest.TestCase):

    @patch('builtins.open', new_callable=mock_open,
           read_data="id;state;date;amount;currency_name;currency_code;from;to;description\n"
                     "650703;EXECUTED;2023-09-05T11:30:32Z;16210;Sol;PEN;Счет 58803664561298323391;Счет 39745660563456619397;Перевод организации\n")
    def test_read_transactions_from_csv_success(self, mock_file):
        # Проверка на успешное чтение CSV
        result = read_transactions_from_csv('dummy_path.csv')

        expected = [{
            'id': '650703',
            'state': 'EXECUTED',
            'date': '2023-09-05T11:30:32Z',
            'amount': '16210',
            'currency_name': 'Sol',
            'currency_code': 'PEN',
            'from': 'Счет 58803664561298323391',
            'to': 'Счет 39745660563456619397',
            'description': 'Перевод организации'
        }]

        self.assertEqual(result, expected)

    @patch('builtins.open', side_effect=FileNotFoundError)
    def test_read_transactions_from_csv_file_not_found(self, mock_file):
        # Проверка на случай, когда файл не найден
        result = read_transactions_from_csv('dummy_path.csv')
        self.assertEqual(result, [])

    @patch('builtins.open', new_callable=mock_open, read_data="")
    def test_read_transactions_from_csv_empty_file(self, mock_file):
        # Проверка на случай пустого файла
        result = read_transactions_from_csv('dummy_path.csv')
        self.assertEqual(result, [])


class TestExcelReader(unittest.TestCase):

    @patch('pandas.read_excel')
    def test_read_transactions_from_excel_success(self, mock_read_excel):
        # Подготовка данных для имитации Excel-файла
        mock_data = pd.DataFrame([{
            'id': '650703',
            'state': 'EXECUTED',
            'date': '2023-09-05T11:30:32Z',
            'amount': '16210',
            'currency_name': 'Sol',
            'currency_code': 'PEN',
            'from': 'Счет 58803664561298323391',
            'to': 'Счет 39745660563456619397',
            'description': 'Перевод организации'
        }])
        mock_read_excel.return_value = mock_data

        # Вызов функции
        result = read_transactions_from_excel('dummy_path.xlsx')

        expected = [{
            'id': '650703',
            'state': 'EXECUTED',
            'date': '2023-09-05T11:30:32Z',
            'amount': '16210',
            'currency_name': 'Sol',
            'currency_code': 'PEN',
            'from': 'Счет 58803664561298323391',
            'to': 'Счет 39745660563456619397',
            'description': 'Перевод организации'
        }]

        self.assertEqual(result, expected)

    @patch('pandas.read_excel', side_effect=FileNotFoundError)
    def test_read_transactions_from_excel_file_not_found(self, mock_read_excel):
        # Проверка на случай, когда Excel файл не найден
        result = read_transactions_from_excel('dummy_path.xlsx')
        self.assertEqual(result, [])

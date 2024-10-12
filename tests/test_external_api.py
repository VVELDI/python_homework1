from unittest.mock import patch

import pytest

from src.external_api import convert_currency


# Тест успешной конвертации
@patch('src.external_api.requests.get')
def test_convert_currency_success(mock_get):
    mock_response = {
        'success': True,
        'query': {'from': 'USD', 'to': 'RUB', 'amount': 100},
        'info': {'rate': 96.0},
        'result': 9600.0
    }
    mock_get.return_value.status_code = 200
    mock_get.return_value.json.return_value = mock_response

    result = convert_currency(100, 'USD')
    assert result == 9600.0


# Тест ошибки API
@patch('src.external_api.requests.get')
def test_convert_currency_api_error(mock_get):
    mock_get.return_value.status_code = 401
    mock_get.return_value.json.return_value = {'message': 'Unauthorized'}

    with pytest.raises(Exception, match="Ошибка API: 401"):
        convert_currency(100, 'USD')


# Тест неправильного ответа
@patch('src.external_api.requests.get')
def test_convert_currency_invalid_response(mock_get):
    mock_response = {
        'success': False,
        'error': {'info': 'Invalid request'}
    }
    mock_get.return_value.status_code = 200
    mock_get.return_value.json.return_value = mock_response

    with pytest.raises(Exception, match="Ошибка при конвертации валюты: {'info': 'Invalid request'}"):
        convert_currency(100, 'USD')

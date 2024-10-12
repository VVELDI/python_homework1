import os
import requests
from dotenv import load_dotenv

# Загрузка переменных окружения из .env файла
load_dotenv()

API_KEY = os.getenv('API_LAYER_KEY')


def convert_currency(amount, from_currency, to_currency="RUB"):
    """Конвертирует валюту с использованием внешнего API."""
    url = f"https://api.apilayer.com/exchangerates_data/convert?to={to_currency}&from={from_currency}&amount={amount}"

    headers = {
        "apikey": API_KEY
    }

    response = requests.get(url, headers=headers)

    if response.status_code == 200:
        data = response.json()
        if data.get('success'):
            return data['result']
        else:
            raise Exception(f"Ошибка при конвертации валюты: {data.get('error', 'Неизвестная ошибка')}")
    else:
        raise Exception(f"Ошибка API: {response.status_code}, {response.json()}")


def get_transaction_amount_in_rubles(transaction):
    """Возвращает сумму транзакции в рублях, если транзакция не в рублях, происходит конвертация."""
    amount = float(transaction['operationAmount']['amount'])
    currency_code = transaction['operationAmount']['currency']['code']
    print(transaction['id'])
    if currency_code == "RUB":
        return amount
    else:
        return convert_currency(amount, currency_code)
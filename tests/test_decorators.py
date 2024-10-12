import datetime

import pytest

from src.decorators import log  # Импортируем декоратор


@log()
def successful_function(a, b):
    return a + b


@log()
def function_with_error(a, b):
    return a / b


def test_successful_function(capsys):
    successful_function(5, 5)
    captured = capsys.readouterr()
    assert "Начало работы функции - successful_function" in captured.out
    assert "Результат выполнения функции: 10" in captured.out
    assert "Функция successful_function завершилась без ошибок" in captured.out


def test_function_with_error(capsys):
    with pytest.raises(ZeroDivisionError):
        function_with_error(1, 0)

    captured = capsys.readouterr()
    assert "Начало работы функции - function_with_error" in captured.out
    assert "Функция function_with_error завершилась с ошибкой" in captured.out
    assert "Входные параметры: (1, 0), {}" in captured.out


def test_successful_function_with_explicit_log_file():
    @log("log.txt")
    def successful_function_with_log(a, b):
        return a + b

    successful_function_with_log(2, 2)
    with open('log.txt', 'r', encoding="utf-8") as file:
        result = file.read()
        data_now = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        assert 'Начало работы функции - successful_function_with_log : ' in result
        assert 'Функция successful_function_with_log завершилась без ошибок:' in result
        assert f"{data_now}" in result
        file.close()

import datetime


def log(filename=None):
    """ Декоратор для логирования начала и завершения работы функции.
      Если указан файл, логи будут записаны в файл. В противном случае
      логи будут выведены в стандартный вывод (консоль)."""
    def decorator(func):
        def wrapper(*args, **kwargs):
            func_name = func.__name__  # Имя оригинальной функции

            if filename:
                time_start = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S.%f")
                with open(filename, 'a', encoding='utf-8') as file:
                    file.write(f'Начало работы функции - {func_name} : {time_start}\n')
                try:
                    result_func = func(*args, **kwargs)
                except Exception as exc_info:
                    time_end = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S.%f")
                    with open(filename, 'a', encoding='utf-8') as file:
                        file.write(f'Функция {func_name} завершилась с ошибкой - {exc_info} : {time_end}\n')
                        file.write(f'Входные параметры: {args}, {kwargs}\n')
                        file.write(f'{"-" * 70}\n')
                    raise
                else:
                    time_end = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S.%f")
                    with open(filename, 'a', encoding='utf-8') as file:
                        file.write(f'Результат выполнения функции: {result_func}\n')
                        file.write(f'Функция {func_name} завершилась без ошибок: {time_end}\n')
                        file.write(f'{"-" * 70}\n')
                    return result_func
            else:
                time_start = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S.%f")
                print(f'Начало работы функции - {func_name} : {time_start}')
                try:
                    result_func = func(*args, **kwargs)
                except Exception as exc_info:
                    time_end = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S.%f")
                    print(f'Функция {func_name} завершилась с ошибкой - {exc_info} : {time_end}')
                    print(f'Входные параметры: {args}, {kwargs}')
                    print(f'{"-" * 70}\n')
                    raise
                else:
                    time_end = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S.%f")
                    print(f"Результат выполнения функции: {result_func}")
                    print(f'Функция {func_name} завершилась без ошибок: {time_end}')
                    print(f'{"-" * 70}\n')
                    return result_func

        return wrapper

    return decorator

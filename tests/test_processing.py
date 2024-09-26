import pytest

import src.processing


@pytest.mark.parametrize("data_dictionary, state_, expected", [
    ([{'id': 41428829, 'state': 'EXECUTED', 'date': '2019-07-03T18:35:29.512364'},  # если state_ отличается от
      {'id': 939719570, 'state': 'EXECUTED', 'date': '2018-06-30T02:08:58.425572'}],  # EXECUTED или 'CANCELED'
     'qwe',  # вернет []
     []),
    ([{'id': 594226727, 'date': '2018-09-12T21:27:25.241689'}],
     "",
     [])
])
def test_filter_by_state(data_dictionary, state_, expected):
    assert src.processing.filter_by_state(data_dictionary, state_) == expected


def test_with_state_executed(default_test_list):
    assert src.processing.filter_by_state(default_test_list, "EXECUTED") == [{'id': 41428829,
                                                                              'state': 'EXECUTED',
                                                                              'date': '2019-07-03T18:35:29.512364'},
                                                                             {'id': 939719570, 'state': 'EXECUTED',
                                                                              'date': '2018-06-30T02:08:58.425572'}]


def test_with_state_canceled(default_test_list):
    assert src.processing.filter_by_state(default_test_list, "CANCELED") == [{'id': 594226727,
                                                                              'state': 'CANCELED',
                                                                              'date': '2018-09-12T21:27:25.241689'},
                                                                             {'id': 615064591, 'state': 'CANCELED',
                                                                              'date': '2018-10-14T08:21:33.419441'}]


@pytest.mark.parametrize("data_dictionary, reverse_flag, expected", [
    ([{'id': 41428829, 'state': 'EXECUTED', 'date': '2019-07-03T18:35:29.512364'},  # для одинаковых date
      {'id': 594226727, 'state': 'CANCELED', 'date': '2018-09-12T21:27:25.241689'},
      {'id': 939719570, 'state': 'EXECUTED', 'date': '2019-07-03T18:35:29.512364'}],
     True,
     [{'id': 41428829, 'state': 'EXECUTED', 'date': '2019-07-03T18:35:29.512364'},
      {'id': 939719570, 'state': 'EXECUTED', 'date': '2019-07-03T18:35:29.512364'},
      {'id': 594226727, 'state': 'CANCELED', 'date': '2018-09-12T21:27:25.241689'},
      ]),
    ([{'id': 41428829, 'state': 'EXECUTED', 'date': '2012.07.03'},  # для нестандартных дат
      {'id': 594226727, 'state': 'CANCELED', 'date': '2018-09-12T21:27:25.241689'},
      {'id': 939719570, 'state': 'EXECUTED', 'date': '2019-07-03T18:35:29.512364'}],
     True,
     [{'id': 41428829, 'state': 'EXECUTED', 'date': 'Формат даты неверный: 2012.07.03'},
      {'id': 939719570, 'state': 'EXECUTED', 'date': '2019-07-03T18:35:29.512364'},
      {'id': 594226727, 'state': 'CANCELED', 'date': '2018-09-12T21:27:25.241689'},
      ]),
    ([{'id': 41428829, 'state': 'EXECUTED', 'date': '07.03'},  # для некорректных дат
      {'id': 594226727, 'state': 'CANCELED', 'date': '2018-09-12T21:27:25.241689'},
      {'id': 939719570, 'state': 'EXECUTED', 'date': '2019-07-03T18:35:29.512364'}],
     True,
     [{'id': 41428829, 'state': 'EXECUTED', 'date': 'Формат даты неверный: 07.03'},
      {'id': 939719570, 'state': 'EXECUTED', 'date': '2019-07-03T18:35:29.512364'},
      {'id': 594226727, 'state': 'CANCELED', 'date': '2018-09-12T21:27:25.241689'},
      ]),
    ([{'id': 41428829, 'state': 'EXECUTED', 'date': '07.03'},  # для некорректного значения ключа
      {'id': 594226727, 'state': 'CANCELED', 'dat': '2018-09-12T21:27:25.241689'}],
     True,
     ["Список не корректен, в одной/нескольких словарях отсутствует ключ 'date'"])
])
def test_sort_by_date(data_dictionary, reverse_flag, expected):
    assert src.processing.sort_by_date(data_dictionary, reverse_flag) == expected


# Тест с флагом по умолчанию True
def test_sort_with_true(default_test_list):
    assert src.processing.sort_by_date(default_test_list, True) == [{'id': 41428829, 'state': 'EXECUTED',
                                                                     'date': '2019-07-03T18:35:29.512364'},
                                                                    {'id': 615064591, 'state': 'CANCELED',
                                                                     'date': '2018-10-14T08:21:33.419441'},
                                                                    {'id': 594226727, 'state': 'CANCELED',
                                                                     'date': '2018-09-12T21:27:25.241689'},
                                                                    {'id': 939719570, 'state': 'EXECUTED',
                                                                     'date': '2018-06-30T02:08:58.425572'}]


# Тест с флагом по умолчанию False
def test_sort_with_false(default_test_list):
    assert src.processing.sort_by_date(default_test_list, False) == [{'id': 939719570,
                                                                      'state': 'EXECUTED',
                                                                      'date': '2018-06-30T02:08:58.425572'},
                                                                     {'id': 594226727, 'state': 'CANCELED',
                                                                      'date': '2018-09-12T21:27:25.241689'},
                                                                     {'id': 615064591, 'state': 'CANCELED',
                                                                      'date': '2018-10-14T08:21:33.419441'},
                                                                     {'id': 41428829, 'state': 'EXECUTED',
                                                                      'date': '2019-07-03T18:35:29.512364'}]

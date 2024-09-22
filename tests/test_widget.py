import pytest

import src.widget


@pytest.mark.parametrize(
    "card_number, expected", [("Visa Platinum 7000792289606361", "Visa Platinum 7000 79** **** 6361"),
                              ("Счет 73654108430135874305", "Счет **4305"),
                              ("Счет 203сс2323424", "Данные не корректны"),
                              ("Счет 7000792289606361", "Данные не корректны"),
                              ("Visa Platinum 73654108430135874305", "Данные не корректны"),
                              ("", "Данные не корректны"),
                              ("Visa", "Данные не корректны")]
)
def test_mask_account_card(card_number, expected):
    assert src.widget.mask_account_card(card_number) == expected
    with pytest.raises(TypeError):
        assert src.widget.mask_account_card({})
    with pytest.raises(TypeError):
        assert src.widget.mask_account_card()


@pytest.mark.parametrize(
    "date_, expected", [("2024-03-11T02:26:18.671407", "11.03.2024"),
                        ("2022-03-11T02:26:18.671407", "11.03.2022"),
                        ("24-03-11T02:26:18.671407", "Формат даты неверный"),
                        ("", "Формат даты неверный"),
                        ([22], "Формат даты неверный"),
                        ({}, "Формат даты неверный"),
                        ("__________", "Формат даты неверный")]
)
def test_get_date(date_, expected):
    assert src.widget.get_date(date_) == expected

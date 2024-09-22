import pytest
from src import masks


@pytest.mark.parametrize("card_number, expected", [
    ("7000792289606361", "7000 79** **** 6361"),
    ("", "Данные не корректны"),
    ("1", "Данные не корректны"),
    ("70007922896063612", "Данные не корректны"),
    ("шшоавыь", "Данные не корректны"), ])
def test_get_mask_card_number(card_number, expected):
    assert masks.get_mask_card_number(card_number) == expected


@pytest.mark.parametrize("account_number, expected", [
    ("73654108430135874305", "**4305"),
    ("", "Данные не корректны"),
    ("1", "Данные не корректны"),
    ("70007922896063612", "Данные не корректны"),
    ("шшоавыь", "Данные не корректны"), ])
def test_get_mask_account(account_number, expected):
    assert masks.get_mask_account(account_number) == expected

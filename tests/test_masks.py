import pytest
from src import masks


@pytest.mark.parametrize("card_number, expected", [
    ("7000792289606361", "7000 79** **** 6361"),
    ("", "Недопустимый номер карты"),
    ("1", "Недопустимый номер карты"),
    ("70007922896063612", "Недопустимый номер карты"),
    ("шшоавыь", "Недопустимый номер карты"), ])
def test_get_mask_card_number(card_number, expected):
    assert masks.get_mask_card_number(card_number) == expected


@pytest.mark.parametrize("account_number, expected", [
    ("73654108430135874305", "**4305"),
    ("", "Недопустимый номер счета"),
    ("1", "Недопустимый номер счета"),
    ("70007922896063612", "Недопустимый номер счета"),
    ("шшоавыь", "Недопустимый номер счета"), ])
def test_get_mask_account(account_number, expected):
    assert masks.get_mask_account(account_number) == expected

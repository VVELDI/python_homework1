import pytest
from src import masks


@pytest.mark.parametrize("card_number, expected", [
    ("", "Данные не корректны"),
    ("1", "Данные не корректны"),
    ("70007922896063612", "Данные не корректны"),
    ("шшоавыь", "Данные не корректны"), ])
def test_get_mask_card_number(card_number, expected):
    assert masks.get_mask_card_number(card_number) == expected


def test_get_mask_default_card_number(default_cart_number):
    assert masks.get_mask_card_number(default_cart_number) == "7000 79** **** 6361"


@pytest.mark.parametrize("account_number, expected", [
    ("", "Данные не корректны"),
    ("1", "Данные не корректны"),
    ("70007922896063612", "Данные не корректны"),
    ("шшоавыь", "Данные не корректны"), ])
def test_get_mask_account(account_number, expected):
    assert masks.get_mask_account(account_number) == expected


def test_get_mask_account_number(default_account_number):
    assert  masks.get_mask_account(default_account_number) == "**4305"

import pytest

import src.widget

@pytest.mark.parametrize(
    "card_number, expected", [("Visa Platinum 7000792289606361", "Visa Platinum 7000 79 ** 6361")]
)
def test_mask_account_card(card_number, expected):
    assert src.widget.mask_account_card(card_number) == expected

import pytest
from bank_app import transfer, calculate_interest


def test_transfer_success():
    from_balance, to_balance = transfer(5000, 2000, 1000)
    assert from_balance == 4000
    assert to_balance == 3000


def test_transfer_insufficient_balance():
    with pytest.raises(ValueError):
        transfer(500, 1000, 800)


def test_transfer_then_interest():
    _, to_balance = transfer(10000, 2000, 5000)
    final_balance = calculate_interest(to_balance, 10, 1)
    assert final_balance == pytest.approx(7700)

import pytest
from memoized_coin_change import dp_make_change, memo_mc


@pytest.mark.parametrize(
    "coin_value_list, change, expected_min_coins",
    [
        ([1, 5, 10, 21, 25], 63, 3),
        ([1, 2, 5], 11, 3),
        ([2, 5], 7, 2),
    ],
)
def test_memo_mc(coin_value_list, change, expected_min_coins):
    known_results = {}

    actual_min_coins = memo_mc(coin_value_list, change, known_results)

    print(f"change: {change}")
    print(f"actual_min_coins: {actual_min_coins}")
    print(f"expected_min_coins: {expected_min_coins}")

    assert actual_min_coins == expected_min_coins, (
        f"Expected {expected_min_coins}, but got {actual_min_coins}"
    )

    assert change in known_results, (
        "The known_results dictionary should contain the result for the input change."
    )


@pytest.mark.parametrize(
    "coin_value_list, change, expected_min_coins",
    [
        ([1, 5, 10, 21, 25], 63, 3),
        ([1, 2, 5], 11, 3),
        ([2, 5], 7, 2),
    ],
)
def test_dp_make_change(coin_value_list, change, expected_min_coins):
    actual_min_coins = dp_make_change(coin_value_list, change)

    print(
        f"change: {change}, expected_min_coins: {expected_min_coins}, actual_min_coins: {actual_min_coins}"
    )

    assert actual_min_coins == expected_min_coins, (
        f"Expected {expected_min_coins}, but got {actual_min_coins}"
    )

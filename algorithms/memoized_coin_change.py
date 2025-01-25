def memo_mc(coin_value_list, change, known_results):
    min_coins = change
    if change in coin_value_list:
        known_results[change] = 1
        return 1
    elif change in known_results:
        return known_results[change]
    else:
        new_coin_list = [c for c in coin_value_list if c <= change]
        for i in new_coin_list:
            num_coins = 1 + memo_mc(coin_value_list, change - i, known_results)
            if num_coins < min_coins:
                min_coins = num_coins
            known_results[change] = min_coins
    return min_coins


def dp_make_change(coin_value_list, change):
    min_coins = [None] * (change + 1)
    for cents in range(change + 1):
        min_coins[cents] = cents
        for c in coin_value_list:
            if cents >= c:
                min_coins[cents] = min(min_coins[cents], min_coins[cents - c] + 1)
    return min_coins[change]


if __name__ == "__main__":
    print(dp_make_change([1, 5, 10, 25], 63))

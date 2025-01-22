def memo_mc(coin_value_list, change, known_results):
    min_coins = change
    if change in coin_value_list:
        known_results[change] = 1
        return 1
    elif change in known_results:
        return known_results[change]
    else:
        for i in [c for c in coin_value_list if c <= change]:
            num_coins = 1 + memo_mc(coin_value_list, change - i, known_results)
            if num_coins < min_coins:
                min_coins = num_coins
            known_results[change] = min_coins
    return min_coins


if __name__ == "__main__":
    print("memoized_coin_change.py")
    print(memo_mc([1, 5, 10, 25], 63, {}))

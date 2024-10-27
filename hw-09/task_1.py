from timeit_decorator import timeit_decorator

@timeit_decorator
def greedy_coin_change(amount, denominations):
    denominations.sort(reverse=True)  # Sort denominations in descending order
    coins_used = {}

    for coin in denominations:
        while amount >= coin:
            if coin in coins_used:
                coins_used[coin] += 1
            else:
                coins_used[coin] = 1
            amount -= coin

    return coins_used

# Example usage
amount_to_change = 113
coin_denominations = [50, 25, 10, 5, 2, 1]

result = greedy_coin_change(amount_to_change, coin_denominations)
print("Coins Used:", result)
print("Total Coins:", sum(result.values()))


@timeit_decorator
def greedy_coin_change_2(amount, denominations):
    denominations.sort(reverse=True)  # Sort denominations in descending order
    coins_used = {}

    for coin in denominations:
        while amount >= coin:
            if coin in coins_used:
                coins_used[coin] += 1
            else:
                coins_used[coin] = 1
            amount -= coin

    return coins_used


result = greedy_coin_change_2(amount_to_change, coin_denominations)
print("Coins Used:", result)
print("Total Coins:", sum(result.values()))

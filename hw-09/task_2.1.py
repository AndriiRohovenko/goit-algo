from timeit_decorator import timeit_decorator

@timeit_decorator
def find_min_coins(sum, coins):
    # Initialize arrays for storing minimum coins required and the last coin used for each sub-sum
    min_coins_required = [0] + [float('inf')] * sum
    coin_used = [0] * (sum + 1)

    # Main dynamic programming loop to compute the minimum coins required for each sub-sum
    for i in range(1, sum + 1):
        for coin in coins:
            print(f"--- sub_sum={i}, coin={coin} ---")
            # Check if using the current coin results in fewer coins for the current sub-sum
            if i >= coin and min_coins_required[i - coin] + 1 < min_coins_required[i]:
                min_coins_required[i] = min_coins_required[i - coin] + 1
                coin_used[i] = coin
        # Print the state of min_coins_required and coin_used tables after each sub-sum
        print(f"Min coins required table: \t{min_coins_required}")
        print(f"Coin used table: \t\t{coin_used}")

    # Reconstruct the coins used to form the original sum
    coins_count = {}
    current_sum = sum
    while current_sum > 0:
        coin = coin_used[current_sum]
        coins_count[coin] = coins_count.get(coin, 0) + 1
        current_sum -= coin

    # Sort the result for easier readability, matching initial denominations order
    coins_count_ordered = {coin: coins_count.get(coin, 0) for coin in coins if coin in coins_count}
    return coins_count_ordered, coin_used



# Main testing function with detailed output
if __name__ == "__main__":
    cases = [
        ([50, 25, 10, 5, 2, 1], 113)
    ]
    functions = [find_min_coins]

    for coins, cash_amount in cases:
        print(f"\nCase for coins: {coins} and sum: {cash_amount}")
        for fun in functions:
            # Measure execution time of the function
            result, coin_used = fun(cash_amount, coins)
            print(f"Result for sum {cash_amount} using {fun.__name__}: {result}")
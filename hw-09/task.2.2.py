from timeit_decorator import timeit_decorator


@timeit_decorator
def find_min_coins_memo(amount, denominations, memo=None):
    if memo is None:
        memo = {}
    
    # Check if we already computed the solution for this amount
    if amount in memo:
        print(f"Returning memoized result for amount {amount}: {memo[amount]}")
        return memo[amount]
    
    # Base case: if amount is 0, we need no coins
    if amount == 0:
        print("Amount is 0, returning empty dictionary")
        return {}
    
    # Initialize variables to keep track of the minimum number of coins needed
    min_count = float('inf')
    best_result = None
    print(f"Trying to find minimum coins for amount {amount}")
    
    # Try each denomination
    for coin in denominations:
        if amount >= coin:
            print(f"Trying coin {coin} for amount {amount}")
            # Recursive call for the remainder (amount - coin)
            result = find_min_coins_memo(amount - coin, denominations, memo)
            print(f"Result for amount {amount - coin} with coin {coin}: {result}")
            
            # Check if this solution is better than what we have
            if result is not None:
                current_count = sum(result.values()) + 1
                print(f"Total coins needed if using coin {coin}: {current_count}")
                
                # Update best result if this option uses fewer coins
                if current_count < min_count:
                    min_count = current_count
                    best_result = result.copy()
                    best_result[coin] = best_result.get(coin, 0) + 1
                    print(f"Updated best result for amount {amount}: {best_result}")
    
    # Store the result in memo to avoid recomputation
    memo[amount] = best_result
    print(f"Memoizing result for amount {amount}: {best_result}")
    return best_result



amount_to_change = 113
denominations = [50, 25, 10, 5, 2, 1]
memo = {}

result = find_min_coins_memo(amount_to_change, denominations, memo)
print("Coins Used:", result)
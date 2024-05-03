#!/usr/bin/python3

def makeChange(coins, total):
    # Initialize dp array
    dp = [float('inf')] * (total + 1)
    dp[0] = 0

    # Iterate through each coin denomination
    for coin in coins:
        # Iterate through range from coin to total + 1
        for j in range(coin, total + 1):
            # Update dp[j]
            dp[j] = min(dp[j], dp[j - coin] + 1)

    # Return result
    return (dp[total] if dp[total] != float('inf') else -1)

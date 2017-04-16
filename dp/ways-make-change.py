def ways_make_change(amount, denominations):
    dp = [0] * (amount+1)
    dp[0] = 1
    for coin in denominations:
        for total in range(coin, amount+1):
            dp[total] = dp[total] + dp[total-coin]
    return dp[amount]

amount = 5
denominations = [1,3,5]
print ways_make_change(amount, denominations)
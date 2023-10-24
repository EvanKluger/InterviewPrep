def coin_combos(coins, amount):
    dp = [0] * (amount + 1)
    dp[0] = 1
    for i in coins:
        for j in range(i,len(dp)):
            dp[j] += dp[j - i]
    return dp[amount]
        


coins = [1, 2, 5]
amount = 5
print(coin_combos(coins, amount))

coins = [2, 3, 5]
amount = 7
print(coin_combos(coins, amount))  # Expected output: 2 (2+5, 2+2+3)


coins = [5, 10, 15]
amount = 20
print(coin_combos(coins, amount))  # Expected output: 2 (10+10, 5+15)

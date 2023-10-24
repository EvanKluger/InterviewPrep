def rod_cutting(prices, n):

    dp = [0] * (n+1)

    for i in range(1, n+1):
        max_val = -float('inf')
        for j in range(1, i+1):
            max_val = max(max_val, prices[j-1] + dp[i-j])
        dp[i] = max_val
    return dp[n]


prices = [1, 5, 8, 9, 10, 17, 17, 20, 24, 30]  # Note: We have a 0 at the beginning to make the list 1-indexed


n = 4
print(rod_cutting(prices, n))
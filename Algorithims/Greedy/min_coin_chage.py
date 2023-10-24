def min_coin_change(coins, amount):
    coins.sort(reverse = True)
    place = 0
    ans = 0
    while amount > 0:
        if coins[place] < amount:
            amount -= coins[place]
            ans += 1
        else:
            while amount < coins[place]:
                place += 1
                if place > len(coins):
                    return -1
            amount -= coins[place]
            ans += 1
    return ans


coins1 = [5, 10, 25, 50, 100]
amount1 = 190
print(min_coin_change(coins1, amount1))  # Expected output: 5, because 190 = 100 + 50 + 25 + 10 + 5

coins2 = [1, 2, 4, 8, 16, 32]
amount2 = 23
print(min_coin_change(coins2, amount2))  # Expected output: 4, because 23 = 16 + 4 + 2 + 1

coins3 = [10, 20, 40, 80, 160]
amount3 = 230
print(min_coin_change(coins3, amount3))  # Expected output: 4, because 230 = 160 + 40 + 20 + 10

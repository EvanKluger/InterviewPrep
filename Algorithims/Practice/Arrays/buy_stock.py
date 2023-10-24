#Best Time to Buy and Sell Stock
#given array of prices whats best day to buy and sell

def buy_stock(arr):
    max_diff = 0
    minimum = float('inf')

    for price in arr:

        if price < minimum:
            minimum = price
        
        max_diff = max(max_diff, price - minimum)
    
    return max_diff

print(buy_stock([7,1,5,3,6,4])) # Expected output: 5 (Buy on day 2 at price 1 and sell on day 5 at price 6)
print(buy_stock([7,6,4,3,1]))   # Expected output: 0 (No transaction is done, i.e., max profit = 0)
print(buy_stock([1,2,3,4,5]))   # Expected output: 4 (Buy on day 1 at price 1 and sell on day 5 at price 5)
print(buy_stock([2,4,1,7]))     # Expected output: 6 (Buy on day 3 at price 1 and sell on day 4 at price 7)
print(buy_stock([3,3,5,0,0,3,1,4])) # Expected output: 4 (Buy on day 4 at price 0 and sell on day 8 at price 4)
print(buy_stock([2,1,4,5,2,9,7]))   # Expected output: 8 (Buy on day 2 at price 1 and sell on day 6 at price 9)
print(buy_stock([3,2,6,5,0,3]))     # Expected output: 4 (Buy on day 2 at price 2 and sell on day 3 at price 6)
print(buy_stock([8,5,3,2]))         # Expected output: 0 (Prices are going down, no profit can be made)
print(buy_stock([]))                # Expected output: 0 (No prices given)
print(buy_stock([3])) 



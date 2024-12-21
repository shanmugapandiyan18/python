def maxProfit(prices):
    # Edge case: if there are fewer than two prices, no profit can be made.
    if len(prices) < 2:
        return 0
    
    # Initialize variables for tracking the profit
    first_buy = -float('inf')   # Maximum profit we can get after the first buy
    first_sell = 0              # Maximum profit we can get after the first sell
    second_buy = -float('inf')  # Maximum profit we can get after the second buy
    second_sell = 0             # Maximum profit we can get after the second sell

    # Traverse through the price list
    for price in prices:
        # Update first_buy: max of keeping the old value or buying at this price
        first_buy = max(first_buy, -price)
        
        # Update first_sell: max of keeping the old value or selling at this price
        first_sell = max(first_sell, first_buy + price)
        
        # Update second_buy: max of keeping the old value or buying again after first sell
        second_buy = max(second_buy, first_sell - price)
        
        # Update second_sell: max of keeping the old value or selling again
        second_sell = max(second_sell, second_buy + price)
    
    # The result is the maximum profit we can get after two sells
    return second_sell

# Test the function with some stock prices
prices = list(map(int, input("Enter stock prices: ").split()))
print(f"Maximum profit with at most 2 transactions: {maxProfit(prices)}")

# 121. Best Time to Buy and Sell Stock

# You are given an array prices where prices[i] is the price of a given stock on the ith day.

# You want to maximize your profit by choosing a single day to buy one stock and choosing a different day in the future to sell that stock.

# Return the maximum profit you can achieve from this transaction. If you cannot achieve any profit, return 0.


# Example 1:

# Input: prices = [7,1,5,3,6,4]
# Output: 5
# Explanation: Buy on day 2 (price = 1) and sell on day 5 (price = 6), profit = 6-1 = 5.
# Note that buying on day 2 and selling on day 1 is not allowed because you must buy before you sell.

# Example 2:

# Input: prices = [7,6,4,3,1]
# Output: 0
# Explanation: In this case, no transactions are done and the max profit = 0.
 

# Constraints:
#     1 <= prices.length <= 105
#     0 <= prices[i] <= 104

from typing import List

# Using Two Pointers:

class Solution0:
    def maxProfit(self, prices: List[int]) -> int:
        profit = 0
        left = 0
        right = 1
        n = len(prices)
        while(right < n):
            if(prices[left] < prices[right]):
                if(profit < prices[right] - prices[left]):
                    profit = prices[right] - prices[left]
            elif(prices[left] > prices[right]):
                left = right
            right += 1
        return profit

# Optimized:

class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        profit = 0
        min_price = prices[0]
        for price in prices:
            if(price < min_price):
                min_price = price
                continue
            if(price > min_price):
                if(price-min_price > profit):
                    profit = price-min_price
        return profit


if __name__ == '__main__':
    solution = Solution()

    # Example 1:

    prices = [7,1,5,3,6,4]
    output = 5
    print('\nTest Case #1')
    print(f'solution.maxProfit(prices="{prices}") = {solution.maxProfit(prices=prices)}')
    print(f'Expected Output: {output}')


    prices = [7,6,4,3,1]
    output = 0
    print('\nTest Case #2')
    print(f'solution.maxProfit(prices="{prices}") = {solution.maxProfit(prices=prices)}')
    print(f'Expected Output: {output}')

    prices = [7,2,5,3,6,1]
    output = 4
    print('\nTest Case #3')
    print(f'solution.maxProfit(prices="{prices}") = {solution.maxProfit(prices=prices)}')
    print(f'Expected Output: {output}')
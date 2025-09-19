# Leetcode Problem 121: Best Time to Buy and Sell Stock
# https://leetcode.com/problems/best-time-to-buy-and-sell-stock/
class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        # initialize the buy to first day value in the list
        buy = prices[0]
        # let the maximum profit to be 0
        max_profit = 0
        # now, loop through each value in prices list
        for price in prices:
            # if the price is less than buy, we update the buy to current price
            if price < buy:
                buy = price
            # else, we find the profit by selling the current price and buy price
            else:
                profit = price - buy
                # make sure, we always have the maximum profit
                max_profit = max(profit, max_profit)
        # finally, return the maximum profit
        return max_profit

print("Time Complexity: O(N)")
print("Space Complexity: O(1)")
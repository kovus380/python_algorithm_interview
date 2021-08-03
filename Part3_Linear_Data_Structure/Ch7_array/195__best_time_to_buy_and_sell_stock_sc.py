# 121 | Best Time to Buy and Sell Stock
# https://leetcode.com/problems/best-time-to-buy-and-sell-stock/
from typing import List


class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        out = 0
        for idx, price in enumerate(prices):
            profit = max(prices[idx : ]) - price
            if profit > out:
                out = profit

        return out

sol = Solution()
prices = [7,1,5,3,6,4]
print(sol.maxProfit(prices))

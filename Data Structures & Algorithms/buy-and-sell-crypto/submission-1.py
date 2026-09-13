class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        i, j = 0, 1
        profit = 0
        maxp = 0

        while j < len(prices):
            if prices[i] < prices[j]:
                profit = prices[j] - prices[i]
                maxp = max(profit, maxp)
            else:
                i = j
            j += 1

        return maxp
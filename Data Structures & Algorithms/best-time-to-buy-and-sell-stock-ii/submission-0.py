class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        n = len(prices)

        l, r = 0, 1
        profit = 0

        while r < n:
            if prices[l] < prices[r]:
                profit += prices[r] - prices[l]
                l = r
            elif prices[l] >= prices[r]:
                l = r
            r += 1

        return profit
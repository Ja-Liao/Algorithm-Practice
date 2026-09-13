class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        n = len(prices)
        if n == 1:
            return 0

        l, r = 0, 1
        maxprofit = 0

        while r < n:
            if prices[l] < prices[r]:
                maxprofit = max(maxprofit, prices[r] - prices[l])
            elif prices[l] >= prices[r]:
                l = r
            r += 1

        return maxprofit
class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        if amount == 0:
            return 0

        dp = [amount + 1] * (amount + 1)
        dp[0] = 0

        for num in range(1, amount + 1):
            for c in coins:
                if num - c >= 0:
                    dp[num] = min(dp[num], 1 + dp[num-c])

        return dp[amount] if dp[amount] != amount + 1 else -1
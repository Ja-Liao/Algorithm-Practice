class Solution:
    def change(self, amount: int, coins: List[int]) -> int:
        # dp = {}

        # def dfs(i, a):
        #     if a == amount:
        #         return 1
        #     if a > amount:
        #         return 0
        #     if i == len(coins):
        #         return 0
        #     if (i, a) in dp:
        #         return dp[(i, a)]

        #     dp[(i, a)] = dfs(i, a + coins[i]) + dfs(i + 1, a)

        #     return dp[(i, a)]

        # return dfs(0, 0)
        dp = [[0] * (len(coins) + 1) for _ in range(amount + 1)]
        dp[0] = [1] * (len(coins) + 1)

        for a in range(1, amount + 1):
            for i in range(len(coins) - 1, -1, -1):
                dp[a][i] = dp[a][i + 1]
                if a - coins[i] >= 0:
                    dp[a][i] += dp[a - coins[i]][i]
        
        return dp[amount][0]


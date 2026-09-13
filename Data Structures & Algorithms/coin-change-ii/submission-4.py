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
        # dp = [[0] * (len(coins) + 1) for _ in range(amount + 1)]
        # dp[0] = [1] * (len(coins) + 1)
        # print(dp)

        # for a in range(1, amount + 1):
        #     for i in range(len(coins) - 1, -1, -1):
        #         dp[a][i] = dp[a][i + 1]
        #         if a - coins[i] >= 0:
        #             dp[a][i] += dp[a - coins[i]][i]
        
        # print(dp)
        # return dp[amount][0]
        # dp = [0] * (amount + 1)
        # dp[0] = 1
        
        # for i in range(len(coins) - 1, -1, -1):
        #     nextDP = [0] * (amount + 1)
        #     nextDP[0] = 1

        #     for a in range(1, amount + 1):
        #         nextDP[a] = dp[a]
        #         if a - coins[i] >= 0:
        #             nextDP[a] += nextDP[a - coins[i]]
        #     dp = nextDP
    
        # return dp[amount]
        # dp = [0] * (amount + 1)
        # dp[0] = 1

        # for coin in coins:
        #     for a in range(coin, amount + 1):
        #         dp[a] += dp[a - coin]

        # return dp[amount]

        n = len(coins)

        dp = [[0] * (amount + 1) for _ in range(n + 1)]

        for i in range(n + 1):
            dp[i][0] = 1

        for i in range(1, n + 1):
            for a in range(1, amount + 1):
                dp[i][a] = dp[i - 1][a]
                if a - coins[i - 1] >= 0:
                    dp[i][a] += dp[i][a - coins[i - 1]]

        return dp[n][amount]
        












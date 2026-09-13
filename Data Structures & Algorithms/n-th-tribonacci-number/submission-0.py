class Solution:
    def tribonacci(self, n: int) -> int:
        dp = {}
        dp[0] = 0
        dp[1] = 1
        dp[2] = 1

        if n < 3:
            return dp[n]

        count = 3

        while count <= n:
            dp[count] = dp[count - 3] + dp[count - 2] + dp[count - 1]
            count += 1

        return dp[n]

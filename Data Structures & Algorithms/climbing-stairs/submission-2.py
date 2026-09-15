class Solution:
    def climbStairs(self, n: int) -> int:
        if n == 0:
            return 0
        if n == 1:
            return 1
        if n == 2:
            return 2

        q = [0]*(n+1)
        q[0] = 0
        q[1] = 1
        q[2] = 2

        for i in range(3, n + 1):
            q[i] = q[i - 1] + q[i - 2]

        return q[-1]
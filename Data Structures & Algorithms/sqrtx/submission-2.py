class Solution:
    def mySqrt(self, x: int) -> int:
        if x == 0:
            return 0

        if x == 1:
            return 1

        for i in range(2, x//2 + 1):
            if i * i > x:
                return res
            res = i

        return res
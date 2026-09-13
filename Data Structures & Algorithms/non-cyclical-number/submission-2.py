class Solution:
    def isHappy(self, n: int) -> bool:
        def sos(n):
            res = 0
            while n:
                digit = n % 10
                digit = digit**2
                res += digit
                n = n // 10

            return res
        
        slow, fast = n, sos(n)

        while slow != fast:
            slow = sos(slow)
            fast = sos(sos(fast))

        return True if fast == 1 else False

        
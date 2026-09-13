from math import gcd

class Solution:
    def gcdOfStrings(self, str1: str, str2: str) -> str:
        # len1, len2 = len(str1), len(str2)

        # def isDivisor(l):
        #     if len1 % l != 0 or len2 % l != 0:
        #         return False
        #     f1, f2 = len1 // l, len2 // l
        #     return str1[:l] * f1 == str1 and str1[:l] * f2 == str2

        # for l in range(min(len1, len2), 0, -1):
        #     if isDivisor(l):
        #         return str1[:l]

        # return ''

        m, n = len(str1), len(str2)
        def isDivisor(i):
            if m % i != 0 or n % i != 0:
                return False
            f1, f2 = m // i, n // i
            return str1[:i] * f1 == str1 and str1[:i] * f2 == str2

        for i in range(min(m, n), 0, -1):
            if isDivisor(i):
                return str1[:i]

        return ""
        

        # if str1 + str2 != str2 + str1:
        #     return ""

        # g = gcd(len(str1), len(str2))
        # return str1[:g]
class Solution:
    def mergeAlternately(self, word1: str, word2: str) -> str:
        res = ''
        n, m = len(word1) - 1, len(word2) - 1
        i, j = 0, 0

        while True:
            if i <= n:
                res += word1[i]
                i += 1
            if j <= m:
                res += word2[j]
                j += 1
            if i > n and j > m:
                return res
            
            
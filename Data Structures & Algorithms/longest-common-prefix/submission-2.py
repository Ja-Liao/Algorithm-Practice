class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        # res = strs[0]

        # for i in range(len(strs[0])):
        #     for words in strs:
        #         if i == len(strs) or s[i] != strs[0][i]:
        #             return s[:i]

        # return strs[0]

        prefix = strs[0]
        for i in range(1, len(strs)):
            j = 0
            while j < min(len(prefix), len(strs[i])):
                if prefix[j] != strs[i][j]:
                    break
                j += 1
            prefix = prefix[:j]

        return prefix
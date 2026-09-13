class Solution:
    def findTargetSumWays(self, nums: List[int], target: int) -> int:
        '''
        one potential way to solve could be using dfs and cache
        keep track of i and amount
        not sure how to build out the 2d grid

        '''
        cache = {}

        def dfs(i, a):
            if i == len(nums):
                return 1 if a == target else 0
            if (i, a) in cache:
                return cache[(i, a)]

            cache[(i, a)] = dfs(i + 1, a + nums[i]) + dfs(i + 1, a - nums[i])

            return cache[(i, a)]

        return dfs(0, 0)
class Solution:
    def findTargetSumWays(self, nums: List[int], target: int) -> int:
        '''
        one potential way to solve could be using dfs and cache
        keep track of i and amount
        not sure how to build out the 2d grid

        '''
        # cache = {}

        # def dfs(i, a):
        #     if i == len(nums):
        #         return 1 if a == target else 0
        #     if (i, a) in cache:
        #         return cache[(i, a)]

        #     cache[(i, a)] = dfs(i + 1, a + nums[i]) + dfs(i + 1, a - nums[i])

        #     return cache[(i, a)]

        # return dfs(0, 0)

        dp = defaultdict(int)
        dp[0] = 1

        for i in range(len(nums)):
            next_dp = defaultdict(int)
            for cur_sum, count in dp.items():
                next_dp[cur_sum + nums[i]] += count
                next_dp[cur_sum - nums[i]] += count

            dp = next_dp

        return dp[target]
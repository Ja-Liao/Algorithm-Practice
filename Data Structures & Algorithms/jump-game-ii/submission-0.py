class Solution:
    def jump(self, nums: List[int]) -> int:
        max_reach = 0
        count = 0
        cur = 0
        for i in range(len(nums) - 1):
            max_reach = max(max_reach, i + nums[i])

            if i == cur:
                count += 1
                cur = max_reach
        return count
        
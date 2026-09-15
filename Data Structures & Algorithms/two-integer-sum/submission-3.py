class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        d = {}

        for i, n in enumerate(nums):
            remainder = target - nums[i]
            if remainder in d:
                return [d[remainder], i]
            d[n] = i
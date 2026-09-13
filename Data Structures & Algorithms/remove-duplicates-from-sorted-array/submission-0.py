class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        # n = len(nums)
        # l = r = 0

        # while r < n:
        #     nums[l] = nums[r]
        #     while r < n and nums[r] == nums[l]:
        #         r += 1
        #     l += 1
        
        # return l
        l = 0
        for r in range(len(nums) - 1):
            if nums[r] != nums[r + 1]:
                nums[l] = nums[r]
                l += 1

        nums[l] = nums[-1]   # write last element
        return l + 1
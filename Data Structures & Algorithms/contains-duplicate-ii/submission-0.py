class Solution:
    def containsNearbyDuplicate(self, nums: List[int], k: int) -> bool:
        if len(nums) == 1:
            return False
        
        l, r = 0, 1
        while r < len(nums):
            if nums[l] == nums[r]:
                return True
            if r - l < k:
                r += 1
            elif l == r - 1:
                l += 1
                r += 1
            else:
                l += 1
                

        return False
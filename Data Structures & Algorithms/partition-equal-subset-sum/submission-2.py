class Solution:
    def canPartition(self, nums: List[int]) -> bool:
        if sum(nums) % 2 == 1:
            return False

        dp = set()
        dp.add(0)
        target = sum(nums) // 2
        
        for i in range(len(nums)):
            if nums[i] > target:
                return False

            if nums[i] == target:
                return True

            nextDP = set()
            for t in dp:
                if (t + nums[i]) == target:
                    return True
                nextDP.add(t + nums[i])
                nextDP.add(t)

            dp = nextDP


        return False
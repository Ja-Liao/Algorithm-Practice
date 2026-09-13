class Solution:
    def canJump(self, nums: List[int]) -> bool:
        n = len(nums)
        # Initialize dp array: True/1 if index is reachable, False/0 otherwise.
        # This matches your proposed structure.
        dp = [False] * n 
        dp[0] = True # Starting index is always reachable
        
        for num in range(1, len(nums)):
            for j in range(num):
                if dp[j] and nums[j] >= num - j:
                    # If both are true, then index 'i' is reachable
                    dp[num] = True
                    break # Optimization: Once 'i' is reachable, stop checking earlier indices 'j'
        
        return dp[n-1]

class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        hashset = Counter(nums)
        max_num = 0
        max_int = 0

        for key, value in hashset.items():
            if value > max_num:
                max_int = key
            max_num = max(max_num, value)

        return max_int
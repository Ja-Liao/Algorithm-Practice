class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        # hashset = Counter(nums)
        # max_num = 0
        # max_int = 0

        # for key, value in hashset.items():
        #     if value > max_num:
        #         max_int = key
        #         max_num = value

        # return max_int
        res = count = 0

        for num in nums:
            if count == 0:
                res = num
            count += 1 if num == res else -1

        return res
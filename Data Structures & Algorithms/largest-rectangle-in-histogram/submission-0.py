class Solution:
    def largestRectangleArea(self, heights: List[int]) -> int:
        # n = len(heights)
        # stk = []
        # max_area = 0

        # for i, height in enumerate(heights):
        #     while stk and height < stk[-1][0]:
        #         h, j = stk.pop()
        #         w = i - j
        #         a = h*w
        #         max_area = max(max_area, a)
        #         start = j
        #     stk.append((height, start))

        # while stk:
        #     h, j = stk.pop()
        #     w = n - j
        #     max_area = max(max_area, h*w)

        # return max_area
        maxArea = 0
        stack = []

        for i, h in enumerate(heights):
            start = i
            while stack and stack[-1][1] > h:
                index, height = stack.pop()
                maxArea = max(maxArea, height * (i - index))
                start = index
            stack.append((start, h))

        for i, h in stack:
            maxArea = max(maxArea, h * (len(heights) - i))

        return maxArea
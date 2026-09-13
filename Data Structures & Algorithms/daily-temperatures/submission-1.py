class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        stack = [] 
        res = [0]* len(temperatures) 

        for i, temp in enumerate(temperatures):
            while stack and temp > stack[-1][1]:
                prev_i, prev_temp = stack.pop()
                res[prev_i] = i - prev_i

            stack.append((i, temp))

        return res
class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        # res = []
        # curr = []

        if not digits:
            return []

        hashmap = {2:'abc', 3:'def',4: 'ghi', 5: 'jkl', 6:'mno', 7:'pqrs', 8:'tuv', 9:'wxyz'}

        res = ['']
        for digit in digits:
            temp = []
            for string in res:
                for char in hashmap[int(digit)]:
                    temp.append(string + char)
            res = temp
        
        return res

        # def backtrack(i):
        #     if i == len(digits):
        #         res.append(''.join(curr))
        #         return

        #     for char in hashmap[int(digits[i])]:
        #         curr.append(char)
        #         backtrack(i + 1)
        #         curr.pop()

        # backtrack(0)
        # return res
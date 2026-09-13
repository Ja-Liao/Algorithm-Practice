class Solution:
    def decodeString(self, s: str) -> str:
        # i = 0
        # def helper():
        #     nonlocal i
        #     res = []
        #     num = 0

        #     while i < len(s):
        #         if s[i].isdigit():
        #             num = num * 10 + int(s[i])
        #         elif s[i] == '[':
        #             i += 1
        #             res.append(num * helper())
        #             num = 0 

        #         elif s[i] == ']':
        #             return ''.join(res)

        #         else:
        #             res.append(s[i])
                
        #         i += 1
                
        #     return ''.join(res)

        # return helper()\\

        stack = []

        for i in range(len(s)):
            if s[i] != ']':
                stack.append(s[i])
            else:
                substr = ''
                while stack[-1] != "[":
                    substr = stack.pop() + substr
                stack.pop()

                k = ''
                while stack and stack[-1].isdigit():
                    k = stack.pop() + k
                stack.append(int(k) * substr)

        return "".join(stack)
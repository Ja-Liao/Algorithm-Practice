class Solution:
    def decodeString(self, s: str) -> str:
        i = 0
        def helper():
            nonlocal i
            res = []
            num = 0

            while i < len(s):
                if s[i].isdigit():
                    num = num * 10 + int(s[i])
                elif s[i] == '[':
                    i += 1
                    res.append(num * helper())
                    num = 0 

                elif s[i] == ']':
                    return ''.join(res)

                else:
                    res.append(s[i])
                
                i += 1
                
            return ''.join(res)

        return helper()
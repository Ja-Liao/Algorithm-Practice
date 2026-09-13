class Solution:
    def isPalindrome(self, s: str) -> bool:
        i, j = 0, len(s) - 1

        while i < j:
            if i < j and not s[i].isalnum():
                i += 1
                continue
            if i < j and not s[j].isalnum():
                j -= 1
                continue
            if s[i].lower() != s[j].lower():
                print(i,j)
                return False
            
            i += 1
            j -= 1
            
            

        return True

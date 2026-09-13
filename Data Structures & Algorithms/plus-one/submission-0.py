class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:
        carry = 1

        for i in range(len(digits) - 1, -1, -1):
            s = digits[i] + carry
            
            if s == 10:
                digits[i] = 0
                carry = 1
            else:
                digits[i] = s
                carry = 0
                break
                
        
        if carry:
            digits.insert(0, 1)

        return digits
            

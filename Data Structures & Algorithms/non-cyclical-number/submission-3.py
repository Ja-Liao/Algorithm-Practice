class Solution:
    def isHappy(self, n: int) -> bool:
        # A set to keep track of sums encountered so far
        seen = set()
        
        def dfs(current_n):
            # 1. Calculate the sum of squares of digits
            summ = 0
            for digit_char in str(current_n):
                # Correction: Use **2 for exponentiation
                summ += int(digit_char) ** 2
            
            # 2. Check for the base cases
            if summ == 1:
                # Happy number found
                return True
            
            if summ in seen:
                # Cycle detected (Not a happy number)
                return False
            
            # 3. Mark the current sum and recurse
            seen.add(summ)
            return dfs(summ)

        return dfs(n)
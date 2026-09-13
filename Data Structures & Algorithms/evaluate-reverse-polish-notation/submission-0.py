class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        operator = {'+', '*', '-', '/'}
        stack = []

        for token in tokens:
            if token not in operator:
                stack.append(int(token))
            else:
                x = stack.pop()
                y = stack.pop()
                if token == "+":
                    stack.append(y + x)
                elif token == "-":
                    stack.append(y - x)
                elif token == "*":
                    stack.append(y * x)
                else:  # token == "/"
                    # Must truncate toward zero
                    stack.append(int(y / x))

        return stack.pop()
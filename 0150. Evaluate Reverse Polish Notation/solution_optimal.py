# DS: Stack
# ALGO:
# Time: O(n). Space: O(n)

class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        stack = []
        # operators = {"+", "-", "*", "/"}
        operators = "+-*/"

        for t in tokens:
            if t in operators:
                if len(stack) < 2:
                    return None

                int2 = stack.pop()
                int1 = stack.pop()

                if t == "+":
                    stack.append(int1 + int2)
                elif t == "-":
                    stack.append(int1 - int2)
                elif t == "*":
                    stack.append(int1 * int2)
                elif t == "/":
                    stack.append(int(int1 / int2))
            else:
                stack.append(int(t))

        if len(stack) > 1:
            return None

        return stack.pop()

# DS: Stack
# ALGO:
# Time: O(n). Space: O(n)

class Solution:
    def isValid(self, s: str) -> bool:
        if len(s) % 2 != 0:
            return False

        stack = []
        brackets_dict = {")": "(", "}": "{", "]": "["}

        for c in s:
            if c in brackets_dict:
                if not stack or brackets_dict[c] != stack[-1]:
                    return False
                stack.pop()
            else:
                stack.append(c)

        return not stack

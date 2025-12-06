# DS: Stack, Deque
# ALGO:
# Time: O(1). Space: O(n)
# Strategy: Only add current val to min stack if <= current min


class MinStack:
    def __init__(self):
        self.main_stack = []
        self.min_stack = []

    def push(self, val: int) -> None:
        self.main_stack.append(val)

        # when val == min, push val to min_stack too.
        # Otherwise, when val is popped, corresopnding val in min_stack is popped too, making min incorrect,
        # and can potentially cause index out of bound for getMin()
        if not self.min_stack or val <= self.min_stack[-1]:
            self.min_stack.append(val)

    def pop(self) -> None:
        removed = self.main_stack.pop()
        if removed == self.min_stack[-1]:
            self.min_stack.pop()

    def top(self) -> int:
        return self.main_stack[-1]

    def getMin(self) -> int:
        return self.min_stack[-1]


# Your MinStack object will be instantiated and called as such:
# obj = MinStack()
# obj.push(val)
# obj.pop()
# param_3 = obj.top()
# param_4 = obj.getMin()

# DS: Stack, Deque
# ALGO:
# Time: O(n). Space: O(n)

from collections import deque


class MinStack:
    def __init__(self):
        self.stack = []
        self.desc_deque = deque()

    def push(self, val: int) -> None:
        self.stack.append(val)
        if not self.desc_deque or val <= self.desc_deque[-1]:
            # if deque is empty or new val <= min element in deque,
            # add val to right end of deque to be the new min
            self.desc_deque.append(val)
        else:
            self.desc_deque.appendleft(val)  # O(1)

    def pop(self) -> None:
        removed = self.stack.pop()
        self.desc_deque.remove(removed)  # O(n)

    def top(self) -> int:
        return self.stack[-1]

    def getMin(self) -> int:
        return self.desc_deque[-1]  # O(1)


# Your MinStack object will be instantiated and called as such:
# obj = MinStack()
# obj.push(val)
# obj.pop()
# param_3 = obj.top()
# param_4 = obj.getMin()

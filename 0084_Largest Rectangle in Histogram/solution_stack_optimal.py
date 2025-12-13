# DS: Array
# ALGO: Monotonic Stack
# Time: O(n). Space: O(n)
"""
1. How it Avoids Repeating (The Efficiency Trick)

A naive solution (checking every bar) is slow because for every bar i, it scans left to find the limit, then scans right to find the limit. This repeated scanning creates the O(n2) complexity.

The stack approach avoids re-scanning by reusing information.
A. Implicit Left Boundaries

The stack eliminates the need to scan left.

    Naive: Start at i, look at i-1, i-2, etc., until you find a smaller number.

    Stack: Because the stack is kept sorted (monotonic), the element sitting directly below the top element stack[-1] is guaranteed to be the nearest smaller number to the left.

    Result: We get the "Left Limit" instantly (O(1)) just by peeking at the stack, without iterating backward.

B. Implicit Right Boundaries

The stack eliminates the need to scan right.

    Naive: Start at i, look at i+1, i+2, etc., until you find a smaller number.

    Stack: We don't actively look for the right boundary. We wait for it to arrive. The algorithm is "lazy." It puts a bar in the waiting room (the stack) and does nothing until we encounter a bar i that is smaller than the top of the stack.

    Result: The moment we see a smaller bar, we know immediately that this is the "Right Limit" for the bar on top of the stack.

Summary Visualization

Imagine the algorithm as a game of Tetris:

    We add blocks (bars) to the stack.

    We never calculate the area for a block until we are forced to remove it because a shorter block is coming in.

    Because we only calculate the area at the moment of removal, and we only remove each block once, we never repeat work.

    
2. The "Life Cycle" Proof (Amortized Analysis)

To understand the complexity, look at what happens to a single bar (index i) throughout the entire execution of the algorithm. A bar can only undergo two operations:

    Pushed onto the stack: This happens exactly once for every index (inside the for loop).

    Popped from the stack: This happens at most once for every index (inside the while loop). Once a bar is popped, it is gone forever; it is never pushed back on.

The Math:

    If you have n elements, there are exactly n PUSH operations.

    Since you cannot pop an empty stack or pop an element twice, there are at most n POP operations.

    The logic inside the loops (calculating width, max(), etc.) takes constant time, O(1).

Total Operations = n (pushes) + n (pops) = 2n. In Big-O notation, we drop constants (2), resulting in O(n).
"""


class Solution:
    def largestRectangleArea(self, heights: List[int]) -> int:
        # Append 0 as imaginery 0-height bar to the right to force the stack to empty at the end
        heights.append(0)
        stack = [-1]
        max_area = 0

        for i in range(len(heights)):
            # maintain a monotonically increasing (non-decreasing) stack to leverage natural left and right limit for efficiency.
            # bar at stack top is of interest for area calculation. need to find left, right limits and height limit.

            # when current bar is shorter than bar at stack top, right limit is encountered.
            # keep popping bar at stack top until current bar is taller than bar at stack top, maintaining a non-decreasing stack.
            while stack[-1] != -1 and heights[i] <= heights[stack[-1]]:
                # for each bar popped from stack top, calculate max area:

                # 1. Identify the bar that serves as the height
                # height is limited by height of popped bar itself
                # because any popped bar to the right of current popped bar is at least as tall as current popped bar.
                # popped bars to the right of current popped bar won't be revisited, ensuring O(n) time efficiency.
                h = heights[stack.pop()]

                # 2. Identify the width
                # Right boundary: i (the current shorter bar, fixed for all while loops in each for loop)
                # Left boundary: stack[-1] (the new top after popping)
                w = i - stack[-1] - 1

                max_area = max(max_area, h * w)

            # push current bar onto stack, maintaining non-decreasing stack
            stack.append(i)

        return max_area

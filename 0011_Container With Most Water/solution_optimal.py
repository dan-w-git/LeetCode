# DS: Array
# ALGO: Two Pointers
# Time: O(n). Space: O(1)

"""
Greedy approach results in optimal solution.

Starting from max width, the shorter line is the limiting factor --
With the limiting height, current area is the max area achievable no matter how we pick the other line,
because we can only move the pointers inward (moving pointers outward would visit combinations previously visited).
We can safely discard the shorter line for future considerations and move pointer for shorter line inward.

By moving the pointer for the shorter line, we have a shot for finding a longer line that could compensate
for the decreased width.
"""


class Solution:
    def maxArea(self, height: List[int]) -> int:
        # two pointers
        left = 0
        right = len(height) - 1
        area = 0
        while left < right:
            height_left = height[left]
            height_right = height[right]
            distance = right - left

            if height_left <= height_right:
                area = max(area, height_left * distance)
                left += 1
            else:
                area = max(area, height_right * distance)
                right -= 1

        return area

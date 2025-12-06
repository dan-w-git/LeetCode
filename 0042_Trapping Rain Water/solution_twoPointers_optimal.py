# DS: Array
# ALGO: Two Pointers
# Time: O(n). Space: O(1)
"""
How water trapped is determined at each index:
Let max_left and max_right be max wall heights encountered so far when two pointers start from two ends of array.
Imagine a max water level between max_left and max_right.
Water trapped at a given index is limited by the shorter of max_left and max_right.

Why moving pointer at the limiting wall:
To determine water trapped at the next index, we have to move pointer at the limiting wall (i.e. the shorter of max_left and max_right). If we move pointer at the non-limiting wall, we can't determine the max water level so far, thus can't determine water trapped at the next index.
"""

from typing import List


class Solution:
    def trap(self, height: List[int]) -> int:
        if not height or len(height) < 3:
            return 0

        left = 0
        right = len(height) - 1
        max_left = 0
        max_right = 0
        total_water = 0

        while left < right:
            # Check the shorter wall
            if height[left] < height[right]:
                # The left side is the limiting factor

                if height[left] >= max_left:
                    # Current bar is the new max_left, no water trapped here
                    max_left = height[left]
                else:
                    # Water trapped is the difference between the max wall and the current bar
                    total_water += max_left - height[left]

                # Move the left pointer inwards
                left += 1

            else:
                # The right side is the limiting factor (height[right] <= height[left])

                if height[right] >= max_right:
                    # Current bar is the new max_right, no water trapped here
                    max_right = height[right]
                else:
                    # Water trapped is the difference between the max wall and the current bar
                    total_water += max_right - height[right]

                # Move the right pointer inwards
                right -= 1

        return total_water

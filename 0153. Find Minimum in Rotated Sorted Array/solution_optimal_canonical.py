# DS: Array
# ALGO: Binary Search
# Time: O(logn). Space: O(1)
"""
Comparison,     Status,     Reason
vs nums[right], Best,       Handles rotated & sorted cases in one loop.
vs nums[0],     Valid,      Works only if you filter out the sorted case first.
vs nums[left],  Invalid,    "Fails because the ""reference"" changes and creates ambiguity when you zoom into sorted sub-segments."
"""


class Solution:
    def findMin(self, nums: List[int]) -> int:
        left = 0
        right = len(nums) - 1
        while left < right:
            mid = (left + right) // 2

            if nums[mid] > nums[right]:
                # cliff at right. mid cannot be min
                left = mid + 1
            else:
                # cliff at left. mid can be min. works for sorted array too
                right = mid

        return nums[right]


# [0, 1, 2, 3, 4, 5]
# [5, 0, 1, 2, 3, 4]
# [1, 2, 3, 4, 5, 0]

# [2, 1]

# DS: Array
# ALGO: Negative Marking
# Time: O(n). Space: O(1)
# Doesn't satisfy requirement of not modifying array, but good technique to master

class Solution:
    def findDuplicate(self, nums: List[int]) -> int:
        for num in nums:
            if nums[abs(num)] < 0:
                return abs(num)

            nums[abs(num)] *= -1


"""
[1,3,4,2,2]
[1,-3,4,2,2]
[1,3,4,-2,2]
[1,3,-4,2,2]
[1,3,4,2,-2]: -4 found. 2 is duplicate
"""

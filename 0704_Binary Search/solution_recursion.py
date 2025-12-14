# DS: Array
# ALGO: Resursive Binary Search
# Time: O(logn). Space: O(logn)
"""
Time complexity:
Depth of search tree is the number of times array is split in halves: log_2(n)

Space complexity:
Each time binarySearch function is called, it's added to call stack till it returns a value.
Worse case: log_2(n) number of function calls.
"""


class Solution:
    def search(self, nums: List[int], target: int) -> int:
        def binarySearch(start: int, end: int) -> int:
            """takes in start and end index and target for binary search.
            returns index of number matching target or -1 if target outside limits"""

            # check if target is within bounds to avoid an extra recursive call (occurs if using start > end condition check)
            if target < nums[start] or target > nums[end]:
                return -1

            mid = (start + end) // 2
            if target == nums[mid]:
                return mid
            elif target < nums[mid]:
                return binarySearch(start, mid - 1)
            else:
                return binarySearch(mid + 1, end)

        return binarySearch(0, len(nums) - 1)

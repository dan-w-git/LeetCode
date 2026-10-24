# DS: Array
# ALGO: Binary Search
# Time: O(logn). Space: O(1)

class Solution:
    def findMin(self, nums: List[int]) -> int:
        n = len(nums)
        if n == 1:
            return nums[0]

        left = 0
        right = n - 1

        # already sorted
        if nums[right] > nums[0]:
            return nums[0]

        while left <= right:
            mid = (left + right) // 2

            # proactively check for cliff
            if nums[mid] > nums[mid + 1]:
                return nums[mid + 1]
            if nums[mid - 1] > nums[mid]:
                return nums[mid]

            if nums[mid] > nums[0]:
                left = mid + 1
            else:
                right = mid - 1


# [0, 1, 2, 3, 4, 5]
# [5, 0, 1, 2, 3, 4]
# [1, 2, 3, 4, 5, 0]

# [2, 1]

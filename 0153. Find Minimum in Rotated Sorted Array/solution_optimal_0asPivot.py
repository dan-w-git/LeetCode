# DS: Array
# ALGO: Binary Search
# Time: O(logn). Space: O(1)

class Solution:
    def findMin(self, nums: List[int]) -> int:
        # already sorted
        if nums[0] <= nums[-1]:
            return nums[0]

        left = 0
        right = len(nums) - 1
        while left < right:
            mid = (left + right) // 2

            # if using nums[mid] >= nums[left], when nums[mid] is min, left will still be advanced, missing min.
            if nums[mid] >= nums[0]:
                left = mid + 1
            else:
                right = mid

        return nums[left]


# [0, 1, 2, 3, 4, 5]
# [5, 0, 1, 2, 3, 4]
# [1, 2, 3, 4, 5, 0]

# [2, 1]

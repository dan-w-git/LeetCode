# DS: Array
# ALGO: Binary Search
# Time: O(logn). Space: O(1)

class Solution:
    def search(self, nums: List[int], target: int) -> int:
        left, right = 0, len(nums) - 1

        while left <= right:
            mid = (left + right) // 2
            if nums[mid] == target:
                return mid

            # 1. Check if Left side is sorted
            if nums[mid] >= nums[left]:
                if nums[left] <= target < nums[mid]:
                    right = mid - 1
                else:
                    left = mid + 1
            # 2. Otherwise, Right side is sorted
            else:
                if nums[mid] < target <= nums[right]:
                    left = mid + 1
                else:
                    right = mid - 1
        return -1


# [0, 1, 2, 3, 4, 5]

# [1, 2, 3, 4, 5, 0]. target = 5

# [5, 0, 1, 2, 3, 4]. target = 0

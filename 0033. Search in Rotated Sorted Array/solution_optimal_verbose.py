# DS: Array
# ALGO: Binary Search
# Time: O(logn). Space: O(1)
"""
nums = [4, 5, 6, 7, 0, 1, 2] Imagine we have narrowed the search to the subarray [0, 1, 2].

    left index is 4 (value 0).

    right index is 6 (value 2).

    mid index is 5 (value 1).

Solution 1 (Global Reference):

    Concept: It splits the array into two distinct shelves: the "Bigs" (left of rotation) and the "Smalls" (right of rotation).

    Logic: It uses nums[0] as a static anchor. If nums[mid] >= nums[0], you are on the Big shelf. If not, you are on the Small shelf.

    Result: In the example above (1 >= 4 is False), it correctly identifies that we are in the "Small" section. It then checks if the target lies to the right of mid.

Solution 2 (Local Reference):

    Concept: It doesn't care about the global rotation. It only asks, "Is the line from left to mid continuous and sorted?"

    Logic: It uses the dynamic nums[left] as the anchor.

    Result: In the example above (1 >= 0 is True), it correctly identifies that the range 0 -> 1 is sorted. It then checks if the target lies within this sorted range.
"""


class Solution:
    def search(self, nums: List[int], target: int) -> int:
        n = len(nums)
        if n == 1:
            if nums[0] == target:
                return 0
            else:
                return -1

        left = 0
        right = n - 1

        if nums[left] < nums[right]:  # sorted
            while left <= right:
                mid = (left + right) // 2

                if target == nums[mid]:
                    return mid
                elif target < nums[mid]:
                    right = mid - 1
                else:  # target > nums[mid]
                    left = mid + 1

        else:  # rotated
            while left <= right:
                mid = (left + right) // 2

                if target == nums[mid]:
                    return mid

                # subarray on mid's left is sorted
                elif nums[mid] >= nums[0]:
                    if target >= nums[left] and target < nums[mid]:
                        # target in left array
                        right = mid - 1
                    else:
                        left = mid + 1

                # subarray on mid's right is sorted
                else:  # nums[mid] < nums[0]
                    if target > nums[mid] and target <= nums[right]:
                        # target in right array
                        left = mid + 1
                    else:
                        right = mid - 1

        return -1


# [0, 1, 2, 3, 4, 5]

# [1, 2, 3, 4, 5, 0]. target = 5

# [5, 0, 1, 2, 3, 4]. target = 0

# DS: Array
# ALGO: Two Pointers
# Time: O(n). Space: O(1)

class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        # two pointers
        left = 0
        right = len(numbers) - 1
        while left < right:
            two_sum = numbers[left] + numbers[right]
            if two_sum == target:
                return [left + 1, right + 1]
            if two_sum < target:
                left += 1
            if two_sum > target:
                right -= 1
        return []

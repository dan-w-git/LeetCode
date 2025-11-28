# DS: Array, Dictionary / HashMap
# ALGO:
# Time: O(n), Space: O(n)

class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        seen = {}  # number, index seen so far

        for i, num in enumerate(nums):
            complement = target - num
            if complement in seen:
                return [seen[complement], i]
            seen[num] = i

        return []

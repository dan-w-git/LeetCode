# DS: Array, Set
# ALGO:
# Time: O(n), Space: O(n)

class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
        seen = set()
        for num in nums:
            if num in seen:
                return True
            else:
                seen.add(num)
        return False

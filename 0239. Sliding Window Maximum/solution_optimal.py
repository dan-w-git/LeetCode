# DS: Array, Deque
# ALGO: Sliding Window
# Time: O(n), Space: O(k)

from collections import deque
from typing import List


class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        # monotonically descreasing deque storing indices
        # front of deque is max
        # storing indices instead of numbers for checking if index has left window
        q = deque()
        res = []

        # right pointer iterates through list. window size is k. left pointer is implicitly i - k + 1
        for i, n in enumerate(nums):
            # remove oldest num (front of deque) if index has left window
            if q and q[0] < i - k + 1:
                q.popleft()

            # Remove indices of elements smaller than current num, ensuring monotonicity
            while q and n >= nums[q[-1]]:
                q.pop()

            # add index of smallest num to end of deque
            q.append(i)

            # when full window size is reached, add max to result
            if i >= k - 1:
                res.append(nums[q[0]])

        return res

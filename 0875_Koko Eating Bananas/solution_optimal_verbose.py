# DS: Array
# ALGO: Binary Search, Minimize Search / Boundary Search
# Time: O(nlog(m)), n = len(piles), m = max(piles). Space: O(1)
"""
Difference between solution 1 (lower < upper) and solution 2 (lower <= upper):
Solution 1 (lower < upper):
Template approach - preferred.
terminate iterations when lower == upper and there's only 1 element in search space,
which is guaranteed to be the result by problem definition.
Since boundary takes on the result value, it's returned directly without tracking result
in a separate variable.

Solution 2 (lower <= upper):
Beginner approach.
Terminate iterations when lower > upper and there's 0 element in search space.
result needs to be tracked in a separate variable as boundaries will overshoot result when they cross.
One more iteration than solution 1.
Slightly faster search space reduction with upper = mid - 1 (vs upper = mid in solution 1)
is not enough to skip a whole step of binary search space reduction.

See Notion for patterns for standard binary search vs boundary / min max search.
"""


import math
from typing import List


class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:

        upper = max(piles)
        lower = 1
        k = upper

        # binary search between lower and upper bounds. compare total hrs required at mid speed against target h
        while lower <= upper:
            mid = (lower + upper) // 2
            hrs = sum(math.ceil(pile / mid) for pile in piles)

            if hrs <= h:
                # store result in k. If returning mid as result, hrs might never match h exactly,
                # in which case "while" loop exits without returning mid
                k = mid
                upper = mid - 1
            else:
                lower = mid + 1

        return k

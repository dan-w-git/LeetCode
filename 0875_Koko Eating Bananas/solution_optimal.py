# DS: Array
# ALGO: Binary Search, Minimize Search / Boundary Search
# Time: O(nlog(m)), n = len(piles), m = max(piles). Space: O(1)

import math
from typing import List


class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        lower = 1
        upper = max(piles)

        while lower < upper:
            mid = (lower + upper) // 2
            hrs = sum(math.ceil(pile / mid) for pile in piles)

            if hrs <= h:
                # workable speed. keep mid
                upper = mid
            else:
                # unworkable speed. discard mid
                lower = mid + 1

        # Now lower == upper, min workable speed found
        return upper

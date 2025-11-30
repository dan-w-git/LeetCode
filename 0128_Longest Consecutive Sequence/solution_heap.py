# DS: Array, Set, Heap
# ALGO:
# Time: O(n). Space: O(n)

import heapq


class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        # base cases
        num_length = len(nums)
        if num_length == 0:
            return 0
        if num_length == 1:
            return 1

        # store elements into set
        nums_set = set()
        for num in nums:
            nums_set.add(num)
        # convert set to list and then to min-heap
        distinct_list = list(nums_set)
        heapq.heapify(distinct_list)
        # keep popping smallest element. keep track of consecutive streaks
        longest_streak = 1
        streak = 1
        previous = heapq.heappop(distinct_list)
        while distinct_list:
            current = heapq.heappop(distinct_list)
            if current - previous == 1:
                streak += 1
                longest_streak = max(longest_streak, streak)
            else:
                longest_streak = max(longest_streak, streak)
                streak = 1
            previous = current
        return longest_streak

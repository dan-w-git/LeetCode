# DS: Array
# ALGO: Heap
# Time: O(nlogk). Space: O(n)

import heapq


class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        # 1. Count Frequencies: O(N)
        freq_dict = {}
        for num in nums:
            freq_dict[num] = freq_dict.get(num, 0) + 1

        min_heap = []

        # 2. Iterate and use Min-Heap: O(M log K), where M is number of unique elements (M <= N)
        for num, freq in freq_dict.items():
            # The heap stores (frequency, number) tuples
            heapq.heappush(min_heap, (freq, num))

            # If size exceeds K, pop the element with the smallest frequency (root of Min-Heap)
            if len(min_heap) > k:
                heapq.heappop(min_heap)

        # 3. Extract results: O(K)
        # We only need the 'num' part of the (freq, num) tuple
        return [num for freq, num in min_heap]

# DS: Array
# ALGO: Bucket Sort
# Time: O(n). Space: O(n)

from typing import List


class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        # 1. Manually Count Frequencies using a Dictionary: O(N)
        # freq_map: {number: count, ...}
        freq_map = {}
        for num in nums:
            freq_map[num] = freq_map.get(num, 0) + 1

        # 2. Initialize Buckets: O(N)
        # Buckets array size is len(nums) + 1.
        # A list or array of size N has indices from 0 to N−1. To access the required index N, the array must have a size of N+1.
        # The index 0 is included in the array but typically remains empty, as we don't store numbers that appear 0 times.
        N = len(nums)
        buckets = [[] for _ in range(N + 1)]

        # 3. Fill the Buckets: O(M), where M is number of unique elements
        # Use frequencies as indices. Index i holds a list of numbers that appear i times.
        for num, freq in freq_map.items():
            buckets[freq].append(num)

        # 4. Extract Top K Elements: O(N)
        result = []
        # Iterate the buckets array backward (from highest frequency N down to 1).
        for i in range(N, 0, -1):
            # Check the list of numbers in the current frequency bucket
            for num in buckets[i]:
                result.append(num)

                # Stop once we have collected K elements.
                if len(result) == k:
                    return result

        return result

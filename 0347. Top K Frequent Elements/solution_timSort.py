# DS: Array
# ALGO: built-in sorting (Timsort in Python)
# Time: O(nlogn). Space: O(n)

class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        # record frequencies of elements in dict
        freq_dict = {}
        for num in nums:
            freq_dict[num] = freq_dict.get(num, 0) + 1

        # sort list on frequencies descending
        freq_list = sorted(freq_dict.items(),
                           key=lambda item: item[1], reverse=True)

        # return sublist with k most frequent elements
        return [item[0] for item in freq_list[:k]]

# DS: Array, Set
# ALGO:
# Time: Amortized O(n). Space: O(n)

"""
1. while loop inside for loop appears to be O(n^2), but is amortized O(n).
Consider the total number of operations performed by the while loop across the entire run of the algorithm.
-- A number is only checked for being a sequence start once.
-- Every number in the set is ONLY visited by the inner while loop one time.

Let's look at the sequence [1,2,3,4]:
    Start at 1: The while loop checks 2, 3, and 4. (3 checks)
    Start at 2: Skipped by the if check (2-1=1 is present).
    Start at 3: Skipped by the if check (3-1=2 is present).
    Start at 4: Skipped by the if check (4-1=3 is present).

In this example, the inner loop only performs 4−1=3 total checks, even though the total sequence length is 4. 
The maximum total number of times a number is ever accessed and checked (either in the outer loop or the inner loop) is constant (at most 2 times).

2. When recording consecutive sequences, must iterate over unique numbers instead of original list that might have duplicates.
Worst case: list contains n duplicates of a single number. while loop runs n times; each while loop iterates over n elements. O(n^2)
"""


class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        if not nums:
            return 0

        # store elements into set
        nums_set = set()
        for num in nums:
            nums_set.add(num)

        # iterate over set to record longest sequence
        longest_seq_len = 0
        for x in nums_set:
            # look for start of consecutive sequence
            if x - 1 not in nums_set:
                y = x + 1
                while y in nums_set:
                    y += 1
                longest_seq_len = max(longest_seq_len, y - x)

        return longest_seq_len

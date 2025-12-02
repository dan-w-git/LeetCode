# DS: Array
# ALGO: Two Pointers
# Time: O(n^2). Space: O(n) for Python in-place sort (Timsort). O(logn) for QuickSort

class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        # -4, -1, -1, 0, 1, 2

        # sort array
        nums.sort()  # O(nlogn)

        # fix one num; apply two pointers for 2sum
        n = len(nums)
        result = []
        # k < i < j, otherwise triplets will be duplicated because same elements are rotating among i, j, k
        # k goes up to n - 3 to leave space for i and j
        for k in range(n - 2):
            # skip duplicated fixed element
            if k > 0 and nums[k] == nums[k-1]:
                continue

            # Pruning: Target is smaller than the smallest possible two-sum from the available window
            if -nums[k] < nums[k+1] + nums[k+2]:
                break  # increasing k will only make -nums[k] smaller/same

            # 2sum algo
            target = -nums[k]
            i = k + 1
            j = n - 1
            while i < j:
                two_sum = nums[i] + nums[j]

                if two_sum == target:
                    result.append([nums[i], nums[j], nums[k]])
                    i += 1
                    j -= 1
                    # skip internal duplicates
                    while i < j and nums[i] == nums[i - 1]:
                        i += 1
                    while i < j and nums[j] == nums[j + 1]:
                        j -= 1
                elif two_sum < target:
                    i += 1
                elif two_sum > target:
                    j -= 1
        return result

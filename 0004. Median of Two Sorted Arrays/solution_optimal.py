# DS: Array
# ALGO: Binary Search
# Time: O(log(min(m,n))). Space: O(1)

class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        m = len(nums1)
        n = len(nums2)

        # By ensuring m <= n, you guarantee that j=(m+n+1)//2​−i will always be between 0 and n.
        if m > n:
            return self.findMedianSortedArrays(nums2, nums1)

        # partition two arrays into L1, L2, R1, R2, ensuring combined L and R are of equal length.
        # binary search in nums1 (shorter array) to find a partition such that max(L1) <= min(R2) and max(L2) <= min(R1).
        # max(L1) <= min(R1) and max(L2) <= min(R2) are always true.
        # In this case, L (L1, L2 combined) and R (R1, R2 combined) form a sorted array.
        # median is found at the partition between L and R

        # m = 0 works correctly too
        left = 0
        right = m

        while left <= right:
            i = left + (right - left) // 2
            # length of (L1 + L2)  = (m + n + 1) // 2
            # len(L1) = i
            # len(L2) = j
            j = (m + n + 1) // 2 - i

            L1 = nums1[i-1] if i > 0 else -math.inf
            R1 = nums1[i] if i < m else math.inf
            L2 = nums2[j-1] if j > 0 else -math.inf
            R2 = nums2[j] if j < n else math.inf

            if L1 <= R2 and L2 <= R1:
                if (m + n) % 2 != 0:  # odd number of elements
                    # median is max(L)
                    return max(L1, L2)
                else:  # even
                    # median is average of max(L) and min(R)
                    return (max(L1, L2) + min(R1, R2)) / 2
            elif L1 > R2:
                # too many elements in L1. push left
                right = i - 1
            else:  # L2 > R1
                # not enough elements in L1. push right
                left = i + 1

        return

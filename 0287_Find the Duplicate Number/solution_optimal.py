# DS: Array. Linked List
# ALGO: Floyd's Cycle Detection
# Time: O(n). Space: O(1)

class Solution:
    def findDuplicate(self, nums: List[int]) -> int:
        # Find intersection
        fast = slow = nums[0]
        while True:
            fast = nums[nums[fast]]
            slow = nums[slow]
            if fast == slow:
                break

        # Find cycle entrance
        fast = nums[0]  # re-start fast pointer from beginning
        while fast != slow:
            fast = nums[fast]
            slow = nums[slow]   # slow pointer continues inside cycle

        return fast


"""
[1,3,4,2,2]
nums[0] = 1
nums[1] = 3
nums[3] = 2
nums[2] = 4
nums[4] = 2

1 -> 3 -> 2 -> 4
            <- 

Entrance of cycle is the duplicated number
fast, slow pointers intersects inside cycle
fast pointer travels twice the distance as slow pointer

L: start to cycle entrance
X: distance from cycle entrance to intersection
C: cycle length
n: number of cycles traveled

2(L + X) = L + X + nC
L + X = nC
L = nC - X

This means if one pointer continues from intersection and the other pointer re-starts from beginning and they move at same speed, they'll meet at cycle entrance,
regardless of how many cycles one pointer spins (n).

"""

# DS: Linked List
# ALGO: Two Pointers
# Time: O(L). Space: O(1). L: length of list

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        # use two pointers with a distance of n + 1 steps.
        # When p1 reaches end, p2 is at node right before the node to remove
        # add dummy in front to handle single node case (two pointers at least 2 steps apart)
        dummy = ListNode(0)
        dummy.next = head
        p1 = p2 = dummy

        for _ in range(n + 1):
            p1 = p1.next

        while p1:
            p1 = p1.next
            p2 = p2.next

        p2.next = p2.next.next  # skip nth node from end

        return dummy.next

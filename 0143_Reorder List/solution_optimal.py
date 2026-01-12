# DS: Linked List
# ALGO: Fast Slow Pointers
# Time: O(n). Space: O(1)

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        """
        Do not return anything, modify head in-place instead.
        """
        if not head.next or not head.next.next:
            return

        # find mid node
        slow = fast = head
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next

        # for even list, slow stops at node right of middle. slow.next is the start of second half (uneven split but works fine for reordering)
        curr = slow.next
        prev = None
        slow.next = None  # cut list in halves to prevent infinite loop

        # reverse second half of list
        while curr:
            temp = curr.next
            curr.next = prev
            prev = curr
            curr = temp

        # zip two lists
        l, r = head, prev

        while r:
            tmp_l, tmp_r = l.next, r.next
            l.next, r.next = r, tmp_l
            l, r = tmp_l, tmp_r

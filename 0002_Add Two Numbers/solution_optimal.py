# DS: Linked List
# ALGO:
# Time: O(max(m, n)). Aux Space: O(1)

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        dummy = ListNode(-1)
        curr = dummy
        carry = 0

        while l1 or l2 or carry:
            # get values from current nodes or 0 if end of list reached
            v1 = l1.val if l1 else 0
            v2 = l2.val if l2 else 0

            # calculate sum and carry
            total = v1 + v2 + carry
            carry = total // 10
            digit = total % 10

            # create new node and advance pointer
            curr.next = ListNode(digit)
            curr = curr.next

            # advance input list pointers
            if l1:
                l1 = l1.next
            if l2:
                l2 = l2.next

        return dummy.next

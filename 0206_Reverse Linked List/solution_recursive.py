# DS: Linked List
# ALGO: Iterative
# Time: O(n). Space: O(n)

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        # Base case: head is empty or end of list reached
        if not head or not head.next:
            return head

        # Recursive call to reach end of list
        new_head = self.reverseList(head.next)

        # Re-wiring by reversing pointers in each recursive call, starting from end of list
        head.next.next = head  # reverse pointer
        head.next = None  # remove original pointer to avoid cycle

        return new_head

# DS: Linked List
# ALGO:
# Time: O(L). Space: O(1). L: length of list

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        # reverse list
        prev, curr = None, head
        while curr:
            temp = curr.next
            curr.next = prev
            prev = curr
            curr = temp

        new_head = prev
        if n == 1:
            new_head = new_head.next  # remove new_head
        else:
            # traverse back to find nth node from end
            prev1, curr1 = None, new_head
            for _ in range(n - 1):
                prev1 = curr1
                curr1 = curr1.next

            prev1.next = curr1.next  # remove nth node

        # start from end again to reverse list back
        prev2, curr2 = None, new_head
        while curr2:
            temp2 = curr2.next
            curr2.next = prev2
            prev2 = curr2
            curr2 = temp2

        return prev2

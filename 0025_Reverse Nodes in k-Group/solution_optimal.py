# DS: Linked List
# ALGO:
# Time: O(n). Space: O(1)

from typing import Optional

# Definition for singly-linked list.


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def reverseKGroup(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        dummy = ListNode(-1, head)
        group_prev = dummy

        # reverse groups of k nodes
        while True:
            kth_node = self.findKthNode(group_prev, k)
            if not kth_node:
                break
            group_next = kth_node.next

            # reverse nodes in a group
            prev = group_next
            curr = group_prev.next
            while curr != group_next:
                temp = curr.next
                curr.next = prev
                prev = curr
                curr = temp

            # connect previous group to current group that was just reversed
            temp = group_prev.next  # first node before reversing / last node after reversing
            group_prev.next = kth_node  # last node before reversing / first node after reversing
            group_prev = temp   # advance group_prev to last node after reversing

        return dummy.next

    def findKthNode(self, curr, k):
        while curr and k > 0:
            curr = curr.next
            k -= 1
        return curr

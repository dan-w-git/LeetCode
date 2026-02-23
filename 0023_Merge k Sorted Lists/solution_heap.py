# DS: Linked List, Heap
# ALGO:
# Time: O(nlogk), Space: O(k). n: total number of nodes. k: number of linked lists
"""
heap has k linked lists after intialization. head of each linked list is the smallest node because each linked list is sorted.
each node is pushed onto and popped from heap once. each heap operation takes O(logk)
"""

from typing import List, Optional
import heapq

# Definition for singly-linked list.


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class NodeWrapper:
    def __init__(self, node):
        self.node = node

    def __lt__(self, other):
        return self.node.val < other.node.val


class Solution:
    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
        if len(lists) == 0:
            return None

        min_heap = []
        dummy = ListNode(-1)
        curr = dummy

        for lst in lists:
            if lst:
                heapq.heappush(min_heap, NodeWrapper(lst))

        while min_heap:
            wrapped_node = heapq.heappop(min_heap)
            curr.next = wrapped_node.node
            curr = curr.next

            if wrapped_node.node.next:
                heapq.heappush(min_heap, NodeWrapper(wrapped_node.node.next))

        return dummy.next

# DS: Linked List, Hash Map
# ALGO:
# Time: O(n). Aux Space: O(1)

"""
# Definition for a Node.
class Node:
    def __init__(self, x: int, next: 'Node' = None, random: 'Node' = None):
        self.val = int(x)
        self.next = next
        self.random = random
"""


class Solution:
    def copyRandomList(self, head: 'Optional[Node]') -> 'Optional[Node]':
        if not head:
            return None

        # create interweaved nodes
        curr = head
        while curr:
            curr.next = Node(curr.val, curr.next)
            curr = curr.next.next

        # set random pointers for copied nodes
        curr = head
        while curr:
            if curr.random:
                curr.next.random = curr.random.next
            # if not curr.random case is implicitly handled as random node defaults to None
            curr = curr.next.next

        # separate two lists
        new_head = head.next
        curr = head
        while curr:
            copy = curr.next
            curr.next = curr.next.next  # i.e. curr.next = curr.next.next
            if copy.next:
                copy.next = copy.next.next
            # if not copy.next case is implicitly handled as last node points to None
            curr = curr.next

        return new_head

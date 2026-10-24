# DS: Linked List
# ALGO:
# Time: O(n^2). Aux Space: O(1)

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

        # create new list with next pointers -- O(n)
        n = 0  # track number of nodes
        curr_old = head
        new_head = Node(curr_old.val)
        curr_new = new_head
        while curr_old:
            curr_old = curr_old.next
            if not curr_old:
                curr_new.next = None
            else:
                curr_new.next = Node(curr_old.val)
            curr_new = curr_new.next
            n += 1

        # create random pointers -- O(n^2)
        curr_old = head
        curr_new = new_head

        while curr_old:
            # get index of random node in old list
            p = curr_old
            p = p.random
            if not p:
                curr_new.random = None

            # number of steps pointer takes to reach null (end of list)
            s = 0
            i_random = 0    # index of random node

            while p:
                p = p.next
                s += 1

            i_random = n - s

            # locate random node in new list and create random pointer
            r = new_head
            while i_random > 0:
                r = r.next
                i_random -= 1
            curr_new.random = r

            # advance pointers
            curr_old = curr_old.next
            curr_new = curr_new.next

        return new_head

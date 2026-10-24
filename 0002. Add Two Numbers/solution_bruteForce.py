# DS: Linked List
# ALGO:
# Time: O(m + n). Aux Space: O(1)

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:

        # convert linked list to num
        def getNumFromLinkedList(l: Optional[ListNode]) -> int:
            num = 0
            decimal = 0
            while l:
                num += l.val * (10 ** decimal)
                decimal += 1
                l = l.next
            return num

        # calculate sum
        sum = getNumFromLinkedList(l1) + getNumFromLinkedList(l2)

        # convert sum to linked list
        quotient = -1
        decimal = 1
        dummy = ListNode(-1)
        curr = dummy
        while quotient != 0:
            divisor = 10 ** decimal
            quotient = sum // divisor
            remainder = sum % divisor
            digit = round(remainder / (divisor / 10))
            curr.next = ListNode(digit)
            curr = curr.next
            decimal += 1
            sum -= remainder

        return dummy.next

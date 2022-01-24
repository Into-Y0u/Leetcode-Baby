# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        dummy = curr = ListNode()
        carry = 0
        while l1 or l2:
            curr.next = ListNode()
            curr = curr.next
            l1_val = l2_val = 0
            if l1:
                l1_val = l1.val
                l1 = l1.next
            if l2:
                l2_val = l2.val
                l2 = l2.next
            curr_val = l1_val + l2_val + carry
            curr.val = curr_val % 10
            carry = curr_val // 10
        if carry:
            curr.next = ListNode(carry)
        return dummy.next

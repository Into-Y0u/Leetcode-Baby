# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def mergeTwoLists(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        if not l1 and not l2  : return None 
        temp1,temp2 = l1 ,l2
        dummy = cur = ListNode()
        while temp1 and temp2 :
            if temp1.val <= temp2.val :
                cur.next = temp1 
                cur = cur.next
                temp1 =  temp1.next
            else :
                cur.next = temp2
                cur = cur.next
                temp2 =  temp2.next
        while temp1:
            cur.next = temp1 
            cur = cur.next
            temp1 =  temp1.next
        
        while temp2:
            cur.next = temp2 
            cur = cur.next
            temp2 =  temp2.next
        return dummy.next

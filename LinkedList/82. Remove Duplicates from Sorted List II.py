# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def deleteDuplicates(self, head: Optional[ListNode]) -> Optional[ListNode]:
        dummy = temp = ListNode()
        
        while head :
            if not head.next or head.val != head.next.val :
                temp.next = head
                temp = temp.next
            else :
                while head.next and head.val == head.next.val :
                    head = head.next
            head = head.next
            temp.next = None
        return dummy.next

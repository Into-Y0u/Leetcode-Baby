class Solution:
    def oddEvenList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        new1 = l1 = ListNode()
        new2 = l2 = ListNode()
    
        while head :
            l1.next = head
            l2.next = head.next
            
            l1 = l1.next
            l2 = l2.next
            
            head = head.next.next if l2 else None
        l1.next = new2.next
        return new1.next

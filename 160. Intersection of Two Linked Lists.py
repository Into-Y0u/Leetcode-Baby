# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def helper(self,l1,l2,m,n):
        while m > n :
            l1 = l1.next
            m-=1
        
        while l1 and l2 :
            if l1 == l2 :
                return l1
            l1 = l1.next
            l2 = l2.next
        return None
        
        
    def getlen(self,node):
        l = 0 
        while node :
            l+=1
            node = node.next
        return l
    
    def getIntersectionNode(self, headA: ListNode, headB: ListNode) -> Optional[ListNode]:
        m = self.getlen(headA)
        n = self.getlen(headB)
        if n > m :
            res = self.helper(headB , headA , n , m)
        else :
            res = self.helper(headA , headB , m,n)
        return res
            

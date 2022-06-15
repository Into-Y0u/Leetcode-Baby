from collections import deque
class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        if not (head or head.next) :
            return None
        arr = []
        
        def helper(node):
            while node :
                arr.append(node)
                node = node.next
            return 
        helper(head)
        
        q = deque(arr)
        
        cur = temp = ListNode()
        i = 0
        while q :
            if i%2 == 0 :
                x = q.popleft()
            else :
                x = q.pop()
            x.next = None
            cur.next = x 
            cur = cur.next
            i+=1
        return temp.next
        
        

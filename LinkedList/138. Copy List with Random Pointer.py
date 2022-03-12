class Solution:
    def copyRandomList(self, head: 'Optional[Node]') -> 'Optional[Node]':
        dicu = {None : None}
        cur = head 
        while cur :
            copy = Node(cur.val)
            dicu[cur] = copy
            cur = cur.next 
        cur = head
        while cur  :
            copy = dicu[cur]
            copy.next = dicu[cur.next]
            copy.random = dicu[cur.random]
            cur = cur.next
        return dicu[head]
        

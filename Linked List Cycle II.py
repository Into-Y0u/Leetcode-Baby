class Solution:
    def detectCycle(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if not head : return 
        vis = set()
        temp = head
        while temp not in vis :
            vis.add(temp)
            if temp.next == None :
                return 
            temp = temp.next
        return temp

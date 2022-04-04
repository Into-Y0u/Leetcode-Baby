# for explanation follow below link :
# https://leetcode.com/problems/swapping-nodes-in-a-linked-list/discuss/1013859/Python3Visualization-Two-Pointers-Solution-with-Explanation

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def swapNodes(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        fast,slow  = head,head
        for i in range(k-1):
            fast = fast.next
        
        first = fast
        while fast.next :
            fast = fast.next
            slow = slow.next
        
        first.val , slow.val = slow.val , first.val 
        
        return head

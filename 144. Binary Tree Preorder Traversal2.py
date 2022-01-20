# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def iterative(self,node) :
        if not node : return 
        q = []
        cur = node
        while q or cur != None:
            if cur :
                q.append(cur)
                cur = cur.left
            else :
                cur = q.pop()
                res.append(cur.val)
                cur = cur.right 
        
        
    def recursive(self,node):
        if node :
            self.recursive(node.left)
            res.append(node.val)
            self.recursive(node.right)
            
    def inorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        global res
        res = []
        # self.recursive(root)
        self.iterative(root)

        return res

        

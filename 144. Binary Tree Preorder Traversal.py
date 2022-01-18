# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def helper(self,root):
        if root :
            res.append(root.val)
            if root.left :
                self.helper(root.left)
            if root.right :
                self.helper(root.right)
                
    def iterative(self,node) :
        if not node : return
        q = collections.deque()
        q.append(node)
        while q :
            x = q.pop()
            res.append(x.val)
            if x.right :
                q.append(x.right)
            if x.left:
                q.append(x.left)
 
                
    def recursive(self, node) :
        if node :
            res.append(node.val)
            if node.left :
                self.recursive(node.left)
            if node.right :
                self.recursive(node.right)

        
    def preorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        global res
        res = []
        
        self.iterative(root)
        
        self.recursive(root) 
        return res

        
        

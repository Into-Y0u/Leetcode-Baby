# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isSymmetric(self, root: Optional[TreeNode]) -> bool:
        if not root : return False 
        
        def help(l,r):
            if l is None and r is None :
                return True
            if l and r and l.val == r.val :
                return help(l.left , r.right) and help(l.right , r.left)
        return help(root,root)
        

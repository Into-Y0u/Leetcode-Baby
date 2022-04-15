class Solution:
    def trimBST(self, root: Optional[TreeNode], low: int, high: int) -> Optional[TreeNode]:
        if not root :
            return None
        root.left = self.trimBST( root.left, low, high)
        root.right = self.trimBST(root.right, low, high)
        
        if root.val in range(low,high+1):
            return root 
        elif root.left is not None :
            return root.left
        else :
            return root.right
        

class Solution:
    def sumOfLeftLeaves(self, root: Optional[TreeNode]) -> int:
        if not root :
            return 0 
        elif root.left and not root.left.left and not root.left.right :
            return root.left.val + self.sumOfLeftLeaves(root.right)
        else :
            return  self.sumOfLeftLeaves(root.left) + self.sumOfLeftLeaves(root.right) 

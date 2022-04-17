class Solution:
    def lowestCommonAncestor(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':
        if (not root) or root == p or root == q  :
            return root
        
        left = self.lowestCommonAncestor( root.left, p, q)
        right = self.lowestCommonAncestor( root.right, p, q)
        if left == None :
            return right
        elif right == None :
            return left 
        else :
            return root
        

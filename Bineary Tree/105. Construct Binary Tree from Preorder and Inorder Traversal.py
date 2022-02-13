class Solution:
    def buildTree(self, preorder: List[int], inorder: List[int]) -> Optional[TreeNode]:
        if not preorder or not inorder :
            return None
        
        root = TreeNode(preorder[0])
        m = inorder.index(root.val)
        
        root.left = self.buildTree(preorder[1:m+1] , inorder[:m])
        root.right = self.buildTree(preorder[m+1:] , inorder[m+1:])
        
        return root

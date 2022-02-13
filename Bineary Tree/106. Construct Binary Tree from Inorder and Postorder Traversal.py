class Solution:
    def buildTree(self, inorder: List[int], postorder: List[int]) -> Optional[TreeNode]:
        if not postorder or not inorder :
            return None
        root = TreeNode(postorder[-1])
        m = inorder.index(root.val)
        root.right = self.buildTree( inorder[m+1:] , postorder[m:-1] )
        root.left = self.buildTree( inorder[:m] , postorder[:m])
        return root

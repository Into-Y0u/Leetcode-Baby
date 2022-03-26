class Solution:
    def rob(self, root: Optional[TreeNode]) -> int:
        
        def dfs(root):
            if not root : return [0,0]
            left = dfs(root.left)
            right = dfs(root.right)
            withroot = root.val  + left[1] + right[1]
            withoutRoot  = max(left) +max( right)
            return [withroot , withoutRoot  ]        

        return max(dfs(root))

class Solution:
    def hasPathSum(self, root: Optional[TreeNode], target: int) -> bool:  
        def dfs (node ,cur) :
            if not node : return False
            cur += node.val 
            if not node.left and not node.right :
                return cur == target 
            return dfs(node.left , cur) or  dfs(node.right , cur) 
        return dfs(root,0)

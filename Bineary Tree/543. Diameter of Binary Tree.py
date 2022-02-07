# O(n) 
class Solution:
    def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        res = [0]
        def dfs(root):
            if not root : return -1
            
            l = dfs(root.left)
            r = dfs(root.right)
            res[0] = max(res[0] , 2 + l + r)
            
            return 1 + max(l , r)      # what this func is returning.. the height
        dfs(root)
        return res[0]

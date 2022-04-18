# Recursive Way 

class Solution:
    def kthSmallest(self, root: Optional[TreeNode], k: int) -> int:
        res = []
        def dfs(node) :
            if not root or len(res) > k :
                return
            if node.left :
                dfs(node.left)
            if node :
                res.append(node.val)
            if node.right :
                dfs(node.right)
            return 
        dfs(root)
        print(res)
        return res[k-1]
      
 
#Iterative Way

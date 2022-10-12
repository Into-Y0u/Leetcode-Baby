class Solution:
    def minDiffInBST(self, root: Optional[TreeNode]) -> int:
        temp =[]
        res = [10000007]
        def dfs(node):
            if not node :
                return 
            dfs(node.left)
            temp.append(node.val)
            if len(temp ) == 2 :
                res[0] = min(res[0] , abs(temp[0] - temp[1]))
                temp.pop(0)
            dfs(node.right)
        dfs(root)
        return res[0]

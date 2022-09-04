class Solution:
    def verticalTraversal(self, root: Optional[TreeNode]) -> List[List[int]]:
        res = []
        dicu = dict()
        
        def dfs(node,col,row):
            if not node :
                return 
            if dicu.get(col):
                dicu[col].append((row , node.val))
            else :
                dicu[col] = [(row , node.val)]
            
            dfs(node.left , col-1 , row + 1)
            dfs(node.right , col + 1 , row + 1)
            
        dfs(root,0,0)
        dicu = sorted(dicu.items())
        for k,v in dicu :
            v.sort()
            level = []
            for p,q in v:
                level.append(q)
            if level :
                res.append(level)
        return res
        

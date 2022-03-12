class Solution:
    def zigzagLevelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        if not root :
            return []
        res = []
        s1 = [root]
        s2 = [] ; level = []
        
        while s1 or s2 :
            while s1 :
                root = s1.pop()
                level.append(root.val)
                if root.left : s2.append(root.left)
                if root.right : s2.append(root.right)
            res.append(level)
            level = []
            
            while s2 :
                root = s2.pop()
                level.append(root.val)
                if root.right : s1.append(root.right)
                if root.left : s1.append(root.left)
            if level != []:
                res.append(level)
                level = []
        return res

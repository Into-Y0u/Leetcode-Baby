from collections import deque
class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        res = []
        if not root : return  
        q = deque()
        q.append(root)
        while q :
            ql = len(q)
            level = []
            for i in range(ql) :
                temp = q.popleft()
                if temp :
                    level.append(temp.val)
                    q.append(temp.left)
                    q.append(temp.right)
            if level :
                res.append(level)
        return res

                
        

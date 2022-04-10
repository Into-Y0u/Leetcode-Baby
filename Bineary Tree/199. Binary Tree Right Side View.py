class Solution:
    def rightSideView(self, root: Optional[TreeNode]) -> List[int]:
        q = deque()
        q.append(root)
        res = []
        while q :
            ql = len(q)
            temp = []
            for i in range(ql):
                x = q.popleft()
                if x :
                    temp.append(x.val)
                    if x.left :
                        q.append(x.left)
                    if x.right :
                        q.append(x.right)
            if temp :
                res.append(temp[-1])
            
        return res

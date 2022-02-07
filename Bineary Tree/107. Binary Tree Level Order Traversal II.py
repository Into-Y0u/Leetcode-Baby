    def levelOrderBottom(self, root: Optional[TreeNode]) -> List[List[int]]:
        res = deque()
        q = collections.deque()
        q.append(root)
        while q :
            ql = len(q)
            level = []
            for i in range(ql):
                node = q.popleft()
                if node:
                    level.append(node.val)
                    q.append(node.left)
                    q.append(node.right)
            if level :
                res.appendleft(level)
        return list(res)

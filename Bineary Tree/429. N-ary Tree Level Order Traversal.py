
class Solution:
    def levelOrder(self, root: 'Node') -> List[List[int]]:
        res = []
        st = [root]
        if not root :
            return 
        
        while st :
            xl = len(st)
            level = []
            for i in range(xl):
                x = st.pop(0)
                if x:
                    level.append(x.val)
                    for ele in x.children:
                        st.append(ele)
            if level :
                res.append(level)
        
        return res
        

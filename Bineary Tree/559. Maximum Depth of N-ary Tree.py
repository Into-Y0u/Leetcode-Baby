class Solution:
    def maxDepth(self, root: 'Node') -> int:
        if not root :
            return 0
                
        st = [root]
        level = 0
        while st :
            xl = len(st)
            for i in range(xl):
                x = st.pop(0)
                for ele in x.children :
                    st.append(ele)
            level += 1
        return level

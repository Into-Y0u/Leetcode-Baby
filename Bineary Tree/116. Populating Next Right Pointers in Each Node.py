from collections import deque
class Solution:
    def connect(self, root: 'Optional[Node]') -> 'Optional[Node]':
        if not root : return 
        st = deque()
        st.append(root)
        while st:
            ql = len(st)
            prev = None
            for i in range(ql) :
                x = st.popleft()
                if x :
                    x.next = prev
                    st.append(x.right)
                    st.append(x.left)
                    prev = x
                
        return root
        

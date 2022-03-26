class Solution:
    def flatten(self, root: Optional[TreeNode]) -> None:
        if not root : return None 
        st = [root]
        while st :
            root = st.pop()
            if root.right :
                st.append(root.right)
            if root.left :
                st.append(root.left)
            root.left = None
            root.right = st[-1] if st else None
        

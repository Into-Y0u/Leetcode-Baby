class Solution:
    def minRemoveToMakeValid(self, s: str) -> str:
        if not s :
            return ""
        s = list(s)
        st = []
        
        for i,n in enumerate(s):
            if n == "(":
                st.append(i)
            elif n == ")" :
                if st :
                    st.pop()
                else :
                    s[i] = ""
            
        while st:
            s[st.pop()] = ""
        return "".join(s)
        
                
            
        

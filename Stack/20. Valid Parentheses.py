class Solution:
    def isValid(self, s: str) -> bool:
        st = []
        for i in s :
            if st :
                if st[-1] == "(" and i == ")" :
                    st.pop()
                elif st[-1] == "{" and i == "}" :
                    st.pop()
                    
                elif st[-1] == "[" and i == "]" :
                    st.pop()
                else :
                    st.append(i)
            else :
                st.append(i)
        if st == []:
            return True
        else :
            return False

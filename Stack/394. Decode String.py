class Solution:
    def decodeString(self, s: str) -> str:
        st = []
        
        for i in s :
            if i != "]":
                st.append(i)
            else :
                subs = ""
                while st[-1] != "[" :
                    subs = st.pop() + subs
                st.pop()
                
                k = ""
                while st and st[-1].isdigit():
                    k = st.pop() + k 
                
                st.append(int(k)*subs)
        return "".join(st)
            

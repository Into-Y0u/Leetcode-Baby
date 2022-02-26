class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        st = []
        res = []
        
        def backtracking(op ,cl):
            if op == cl == n :
                res.append("".join(st))
                return 
            
            if op < n :
                st.append("(")
                backtracking(op+1,cl)
                st.pop()
                
            if cl < op :
                st.append(")")
                backtracking(op,cl+1)
                st.pop()
                
        backtracking(0,0)
        return res

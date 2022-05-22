class Solution:
    def countSubstrings(self, s: str) -> int:
        if not s :
            return 0
        res = 0 
        
        def helper(i,j):
            cnt = 0 
            while i >= 0 and j < len(s) and s[i] == s[j]:
                i-=1
                j+=1
                cnt+=1
            return cnt
        
        for x in range(len(s)):
            res += helper(x,x) + helper(x,x+1)
        return res
        

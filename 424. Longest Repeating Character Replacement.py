class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        dicu = {}
        l = 0 
        res = 0
        mx = 0 
        for r in range(len(s)):
            dicu[s[r]] = 1 + dicu.get(s[r],0)
            mx = max(mx,dicu[s[r]])
            
            while  (r-l+1) - mx > k :
                dicu[s[l]] -= 1
                l+=1
            res = max( res , (r-l+1) )
        return res

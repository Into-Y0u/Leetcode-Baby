class Solution:
    def longestPalindrome(self, s: str) -> str:
        res = "" ;  n = len(s)
        reslen = 0 
        for i in range(n):
            l,r = i,i
            reslen = 0
            while (l >= 0 and r < n) and s[l] == s[r] :
                reslen = r-l+1
                if reslen > len(res):
                    res = s[l:r+1]
                l-=1
                r+=1
            l,r = i,i+1
            reslen = 0
            while (l >= 0 and r < n) and s[l] == s[r] :
                reslen = r-l+1
                if reslen > len(res):
                    res = s[l:r+1]
                l-=1
                r+=1
        return res
            

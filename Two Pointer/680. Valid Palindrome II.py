class Solution:
    def validPalindrome(self, s: str) -> bool:
        def verify(s,l,r,flag):
            while l < r :
                if s[l] != s[r] :
                    if flag :
                        return 0
                    else :
                        return verify(s,l+1,r,1) or verify(s,l,r-1,1)
                else :
                    l+=1
                    r-=1
            return 1
        return verify(s,0,len(s)-1,0)

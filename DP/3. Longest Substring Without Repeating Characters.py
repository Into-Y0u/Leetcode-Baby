class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        dicu = dict() ; res = 0 ; l=0
        for i in range(len(s)) :
            if s[i] in dicu and dicu[s[i]] >= l :
                l = dicu[s[i]] + 1
          
            res = max(res , i-l + 1 )
            dicu[s[i]] =  i 
        
        return res
 

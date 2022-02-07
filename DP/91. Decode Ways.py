class Solution:
    def numDecodings(self, s: str) -> int:
        n = len(s)
        dp = [0]*(n+1)
        dp[n] = 1 
        for i in range(n-1,-1,-1):
            if s[i] != "0":
                dp[i] += dp[i+1]
                
            if ( i+2 <= n and  int(s[i:i+2]) <= 26 and s[i] != "0"  ) :
                dp[i] += dp[i+2]
        
        # print(dp)
        return dp[0]
                

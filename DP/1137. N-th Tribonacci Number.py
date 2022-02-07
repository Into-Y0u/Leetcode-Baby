class Solution:
    def tribonacci(self, n: int) -> int:
        dp = [0,1,1]
        
        for i in range(2,n+1):
            dp.append(dp[i-2]+dp[i-1]+dp[i] )
        return dp[n]
